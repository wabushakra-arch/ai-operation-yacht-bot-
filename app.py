#!/usr/bin/env python3
"""
Yacht Broker Operations Bot - Streamlit Web Interface
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from modules.prompts import get_system_prompt
from modules.operations import OPERATIONS_MENU

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Yacht Broker Operations Bot",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = os.getenv("OPENAI_API_KEY", "")

def get_ai_response(client, user_message, operation_context=""):
    """Get response from OpenAI API."""
    system_prompt = get_system_prompt(operation_context)
    
    st.session_state.conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.conversation_history
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        assistant_message = response.choices[0].message.content
        st.session_state.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main Streamlit application."""
    
    # Header
    st.title("⚓ Yacht Broker Operations Bot")
    st.markdown("### Senior Operations Manager for Yacht Brokerages")
    st.divider()
    
    # Sidebar for API key and settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            value=st.session_state.api_key,
            help="Enter your OpenAI API key. You can get one from https://platform.openai.com/api-keys"
        )
        
        if api_key_input:
            st.session_state.api_key = api_key_input
        
        st.divider()
        
        st.header("📋 Operations")
        st.markdown("""
        **Available Operations:**
        - Sales & Client Management
        - Yacht Listings & Marketing
        - Charter Operations
        - Legal & Compliance
        - Pricing & Market Intelligence
        - Owner Services
        - Daily Operations
        """)
        
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state.conversation_history = []
            st.rerun()
    
    # Check if API key is set
    if not st.session_state.api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to get started.")
        st.info("You can get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=st.session_state.api_key)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.subheader("🎯 Select Operation")
        
        operation_options = {
            "Custom Request": "0",
            **{title: key for key, (title, _) in OPERATIONS_MENU.items()}
        }
        
        selected_operation = st.selectbox(
            "Choose an operation type:",
            options=list(operation_options.keys()),
            index=0
        )
        
        operation_key = operation_options[selected_operation]
    
    with col1:
        st.subheader("💬 Chat Interface")
        
        # Display conversation history
        chat_container = st.container(height=400)
        with chat_container:
            for msg in st.session_state.conversation_history:
                if msg["role"] == "user":
                    with st.chat_message("user", avatar="👤"):
                        st.write(msg["content"])
                else:
                    with st.chat_message("assistant", avatar="⚓"):
                        st.write(msg["content"])
        
        # Input area
        st.divider()
        
        if operation_key != "0":
            _, prompt_template = OPERATIONS_MENU[operation_key]
            st.info(f"📝 **Operation:** {selected_operation}")
        
        user_input = st.text_area(
            "Enter your request:",
            height=100,
            placeholder="Describe what you need help with..."
        )
        
        col_send, col_clear = st.columns([3, 1])
        
        with col_send:
            send_button = st.button("🚀 Send", use_container_width=True, type="primary")
        
        with col_clear:
            if st.button("🔄 Reset", use_container_width=True):
                st.session_state.conversation_history = []
                st.rerun()
        
        if send_button and user_input.strip():
            with st.spinner("Processing..."):
                if operation_key == "0":
                    # Custom request
                    response = get_ai_response(client, user_input)
                else:
                    # Operation-specific request
                    _, prompt_template = OPERATIONS_MENU[operation_key]
                    full_prompt = prompt_template.format(user_input=user_input)
                    response = get_ai_response(client, full_prompt, operation_key)
                
                st.rerun()

if __name__ == "__main__":
    main()
