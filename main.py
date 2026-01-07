#!/usr/bin/env python3
"""
Yacht Broker Operations Bot
Main entry point for the CLI-based operations assistant.
"""

import os
from dotenv import load_dotenv
from colorama import Fore, Style
from modules.bot import YachtBrokerBot

def main():
    """Initialize and run the bot."""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(f"{Fore.RED}Error: OPENAI_API_KEY not found in .env file{Style.RESET_ALL}")
        return
    
    bot = YachtBrokerBot(api_key)
    # Run in focused mode for Sales & Client Management (Option A)
    bot.run(focused_mode="A")

if __name__ == "__main__":
    main()
