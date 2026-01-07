"""
Core bot class for the Yacht Broker Operations Bot.
"""

from colorama import Fore, Style, init
from openai import OpenAI
from modules.prompts import get_system_prompt
from modules.operations import OPERATIONS_MENU

init(autoreset=True)

class YachtBrokerBot:
    """Main bot class for yacht brokerage operations."""
    
    def __init__(self, api_key):
        """Initialize the bot with OpenAI client."""
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"
        self.conversation_history = []
    
    def display_welcome(self):
        """Display welcome message and menu."""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}   YACHT BROKER OPERATIONS BOT")
        print(f"{Fore.CYAN}   Senior Operations Manager for Yacht Brokerages")
        print(f"{Fore.CYAN}{'='*60}\n")
    
    def display_menu(self):
        """Display operations menu."""
        print(f"\n{Fore.GREEN}Select an operation:")
        print(f"{Fore.GREEN}{'-'*40}")
        for key, (title, _) in OPERATIONS_MENU.items():
            print(f"{Fore.YELLOW}{key}{Style.RESET_ALL}. {title}")
        print(f"{Fore.YELLOW}0{Style.RESET_ALL}. Custom Request")
        print(f"{Fore.YELLOW}Q{Style.RESET_ALL}. Quit")
        print(f"{Fore.GREEN}{'-'*40}\n")
    
    def get_ai_response(self, user_message, operation_context=""):
        """Get response from OpenAI API."""
        system_prompt = get_system_prompt(operation_context)
        
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *self.conversation_history
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            assistant_message = response.choices[0].message.content
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        except Exception as e:
            return f"Error: {str(e)}"
    
    def handle_operation(self, operation_key):
        """Handle selected operation."""
        if operation_key not in OPERATIONS_MENU:
            print(f"{Fore.RED}Invalid operation selected.{Style.RESET_ALL}")
            return
        
        title, prompt_template = OPERATIONS_MENU[operation_key]
        print(f"\n{Fore.CYAN}{title}")
        print(f"{Fore.CYAN}{'-'*40}\n")
        
        user_input = input(f"{Fore.YELLOW}Provide details for your request:\n{Style.RESET_ALL}> ")
        
        if user_input.strip():
            full_prompt = prompt_template.format(user_input=user_input)
            response = self.get_ai_response(full_prompt, operation_key)
            print(f"\n{Fore.GREEN}{response}{Style.RESET_ALL}\n")
    
    def handle_custom_request(self):
        """Handle custom user request."""
        print(f"\n{Fore.CYAN}Custom Request")
        print(f"{Fore.CYAN}{'-'*40}\n")
        
        user_input = input(f"{Fore.YELLOW}Enter your request:\n{Style.RESET_ALL}> ")
        
        if user_input.strip():
            response = self.get_ai_response(user_input)
            print(f"\n{Fore.GREEN}{response}{Style.RESET_ALL}\n")
    
    def run(self, focused_mode=None):
        """Run the bot main loop.
        
        Args:
            focused_mode: If provided, run only this operation (e.g., 'A' for Sales & Client Management)
        """
        self.display_welcome()
        
        if focused_mode:
            # Run only the specified operation
            print(f"\n{Fore.CYAN}FOCUSED MODE: Sales & Client Management{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*60}\n")
            while True:
                self.handle_operation(focused_mode)
                cont = input(f"\n{Fore.YELLOW}Continue with another request? (yes/no): {Style.RESET_ALL}").strip().lower()
                if cont not in ['yes', 'y']:
                    print(f"\n{Fore.CYAN}Thank you for using the Yacht Broker Operations Bot. Goodbye!{Style.RESET_ALL}\n")
                    break
        else:
            # Full menu mode
            while True:
                self.display_menu()
                choice = input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}").strip().upper()
                
                if choice == "Q":
                    print(f"\n{Fore.CYAN}Thank you for using the Yacht Broker Operations Bot. Goodbye!{Style.RESET_ALL}\n")
                    break
                elif choice == "0":
                    self.handle_custom_request()
                else:
                    self.handle_operation(choice)
