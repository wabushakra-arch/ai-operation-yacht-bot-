import streamlit as st
import os
from dotenv import load_dotenv
from modules.bot import YachtBrokerBot

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Yacht Broker Operations Bot",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.title("⛵ Yacht Broker Operations Bot")
st.markdown("*Senior Operations Manager for Yacht Brokerages - Powered by OpenAI*")
st.divider()

# Get API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    # Try to get from Streamlit secrets
    try:
        api_key = st.secrets["openai_api_key"]
    except:
        st.error("⚠️ OPENAI_API_KEY not configured. Please add it to .env or Streamlit secrets.")
        st.stop()

# Initialize bot
@st.cache_resource
def initialize_bot(api_key):
    return YachtBrokerBot(api_key)

bot = initialize_bot(api_key)

# Sidebar - Operation Selection
st.sidebar.title("📋 Operations Menu")
st.sidebar.markdown("---")

operations = {
    "A": ("Sales & Client Management", "Draft professional communications, questionnaires, and offers"),
    "B": ("Yacht Listings & Marketing", "Create luxury yacht descriptions and marketing materials"),
    "C": ("Charter Operations", "Generate agreements, itineraries, and checklists"),
    "D": ("Legal & Compliance", "Explain contracts and flag compliance risks"),
    "E": ("Pricing & Market Intelligence", "Provide comparable analysis and negotiation strategies"),
    "F": ("Owner Services", "Draft owner reports and performance summaries"),
    "G": ("Daily Operations", "Create viewings, surveys, and closing checklists"),
}

selected_op = st.sidebar.radio(
    "Choose an operation:",
    ["A", "B", "C", "D", "E", "F", "G"],
    format_func=lambda x: f"{x}. {operations[x][0]}"
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**{operations[selected_op][0]}**")
st.sidebar.markdown(f"*{operations[selected_op][1]}*")

# Main Content Area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"📝 {operations[selected_op][0]}")
    st.markdown(operations[selected_op][1])
    st.markdown("---")
    
    # Input area
    st.markdown("### Provide Details for Your Request:")
    user_input = st.text_area(
        "Enter your request:",
        placeholder="E.g., Draft a professional response to a client interested in a 50ft cruising catamaran, €800k budget",
        height=120,
        key="user_input"
    )
    
    # Submit button
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        submit_button = st.button("🚀 Generate Response", use_container_width=True)
    
    with col_btn2:
        clear_button = st.button("🔄 Clear Input", use_container_width=True)
    
    if clear_button:
        st.rerun()
    
    # Process input
    if submit_button:
        if not user_input.strip():
            st.warning("⚠️ Please provide details for your request.")
        else:
            with st.spinner("⏳ Generating professional response..."):
                try:
                    # Get AI response
                    response = bot.get_ai_response(user_input, selected_op)
                    
                    # Display response
                    st.markdown("---")
                    st.markdown("### 📄 Generated Response:")
                    st.markdown(response)
                    
                    # Copy button
                    st.text_area(
                        "Copy the response:",
                        response,
                        height=200,
                        disabled=True,
                        key="response_area"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

with col2:
    st.markdown("### 📊 Quick Reference")
    
    for key in ["A", "B", "C", "D", "E", "F", "G"]:
        if key == selected_op:
            st.info(f"**{key}. {operations[key][0]}**")
        else:
            st.caption(f"{key}. {operations[key][0]}")
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    tips = [
        "✅ Be specific with yacht details",
        "✅ Include budget ranges",
        "✅ Mention location (Mediterranean, Caribbean)",
        "✅ Include timeline information",
        "✅ Review output before sending to clients"
    ]
    for tip in tips:
        st.caption(tip)

# Footer
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.caption("🔒 Your data is processed securely")

with col_f2:
    st.caption("⚖️ Always review AI-generated content")

with col_f3:
    st.caption("📝 For legal advice, consult professionals")
