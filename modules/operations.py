"""
Operations menu and prompt templates for the yacht operations bot.
"""

OPERATIONS_MENU = {
    "A": (
        "SALES & CLIENT MANAGEMENT",
        """Draft a professional communication for a yacht sales scenario:
        
Details provided: {user_input}

Provide a ready-to-use response (email, message, or form) that is professional, 
clear, and tailored to the specific request. Include relevant follow-up questions if needed."""
    ),
    "B": (
        "YACHT LISTINGS & MARKETING",
        """Create or rewrite a yacht listing description:
        
Yacht details: {user_input}

Generate a luxury-focused description suitable for marketing. Include:
- Key highlights
- Technical specs presentation
- Buyer appeal points
- Optional: short and long version options"""
    ),
    "C": (
        "CHARTER OPERATIONS",
        """Prepare charter documentation or guidance:
        
Request: {user_input}

Provide ready-to-use charter templates, explanations, or checklists. Include clear language 
for clients about fees, terms, and procedures."""
    ),
    "D": (
        "LEGAL & COMPLIANCE",
        """Provide legal guidance or compliance support:
        
Question: {user_input}

Explain the concept clearly in plain English. Flag any red flags if applicable. 
Remember: Do not give legal advice—only explain concepts and flag risks."""
    ),
    "E": (
        "PRICING & MARKET INTELLIGENCE",
        """Analyze pricing and provide market guidance:
        
Scenario: {user_input}

Provide comparable analysis, pricing guidance, and negotiation strategy. 
Include market trends if relevant."""
    ),
    "F": (
        "OWNER SERVICES",
        """Create owner-focused documentation:
        
Request: {user_input}

Generate owner reports, performance summaries, or crew management guidance. 
Use professional but accessible language."""
    ),
    "G": (
        "DAILY OPERATIONS",
        """Create operational checklists and SOPs:
        
Task: {user_input}

Generate a ready-to-use checklist or procedure. Include all relevant steps, 
approval checkpoints, and quality controls."""
    ),
}
