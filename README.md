# Yacht Broker Operations Bot

A professional operations assistant for yacht brokerage businesses, powered by OpenAI.

## Features

- **Sales & Client Management** – Draft emails, questionnaires, offers, and buyer comparisons
- **Yacht Listings & Marketing** – Create luxury yacht descriptions and marketing materials
- **Charter Operations** – Generate agreements, itineraries, and checklists
- **Legal & Compliance** – Explain contracts and flag compliance risks
- **Pricing & Market Intelligence** – Provide comparable analysis and negotiation strategies
- **Owner Services** – Draft owner reports and performance summaries
- **Daily Operations** – Create viewings, survey, and closing checklists

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key
Copy `.env.example` to `.env` and add your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your API key
```

### 3. Run the Bot
```bash
python main.py
```

## Usage

The bot provides an interactive CLI menu with predefined operations:

```
A. Sales & Client Management
B. Yacht Listings & Marketing
C. Charter Operations
D. Legal & Compliance
E. Pricing & Market Intelligence
F. Owner Services
G. Daily Operations
0. Custom Request
Q. Quit
```

Select an operation and provide details. The bot will generate professional, ready-to-use output.

## Project Structure

```
ai operation bot/
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
├── README.md              # This file
└── modules/
    ├── __init__.py
    ├── bot.py             # Core bot logic
    ├── prompts.py         # System prompts and contexts
    └── operations.py      # Menu and operation templates
```

## Notes

- The bot is designed for professional brokers, not as legal counsel
- Always review AI-generated output before sending to clients
- For jurisdiction-specific questions, consult with legal professionals
- The conversation history is maintained within a session for context

## Support

For issues or feature requests, modify the modules and extend as needed.
