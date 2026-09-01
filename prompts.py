from langchain_core.prompts import ChatPromptTemplate

# --- CHAIN 1: ACCOUNT STRATEGY PROCESSING PROMPT ---
STRATEGY_SYSTEM = (
    "USE-CASE GUARDRAIL CONSTRAINT:\n"
    "You are an isolated Account Strategy Assistant. Your single focus is to extract corporate goals "
    "and active strategic directions from raw data. Reject casual talk or coding requests.\n\n"
    "Analyze the client details for a sales rep trying to sell '{prod_name}' to a '{target_buyer}'."
)
STRATEGY_HUMAN = (
    "Inbound Raw Web Text:\n{target_context}\n\n"
    "Identify: 1. Core Corporate Priorities, 2. Associated Tech Stack Signals, 3. Immediate operational pain points."
)
STRATEGY_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", STRATEGY_SYSTEM),
    ("human", STRATEGY_HUMAN)
])

# --- CHAIN 2: COMPETITOR MAPPING PROMPT ---
RESEARCH_SYSTEM = (
    "USE-CASE GUARDRAIL CONSTRAINT:\n"
    "You are a Product Research Assistant. Your job is to take an account's strategy summary "
    "and cross-reference it against these target competitors: '{competitors_str}'."
)
RESEARCH_HUMAN = (
    "Account Strategy Analysis:\n{strategy_analysis}\n\n"
    "Raw Ingested Competitor Logs:\n{competitor_context}\n\n"
    "Identify: 1. Specific areas where specified competitors are vulnerable, 2. Counter-positioning angles."
)
RESEARCH_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", RESEARCH_SYSTEM),
    ("human", RESEARCH_HUMAN)
])

# --- CHAIN 3: STRATEGIC REACTION RECOMMENDATOR PROMPT ---
RECOMMENDATION_SYSTEM = (
    "You are a Sales Recommendation Assistant. Use the strategy analysis, competitor insights, and collateral sheets "
    "to write a clean tactical summary. Then, invoke the inventory tool if you need to verify our solution's module availability."
)
RECOMMENDATION_HUMAN = (
    "Customer Strategy:\n{strategy_analysis}\n\n"
    "Competitor Research:\n{research_analysis}\n\n"
    "Collateral Asset Sheet:\n{deck_text}"
)
RECOMMENDATION_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", RECOMMENDATION_SYSTEM),
    ("human", RECOMMENDATION_HUMAN)
])

# --- CHAIN 4: STRUCTURAL PITCH PLAYBOOK GENERATOR PROMPT ---
PLAYBOOK_SYSTEM = (
    "You are an elite B2B Sales Enablement Agent. Your job is to take a completely synthesized set of data inputs "
    "and structure them into a Pydantic object. No conversational chat allowed."
)
PLAYBOOK_HUMAN = (
    "Account Information: {target_company_url}\n"
    "Strategic Analysis Matrix:\n{strategy_analysis}\n\n"
    "Rival Landscape Context:\n{research_analysis}\n\n"
    "Final Recommendations Profile:\n{recommendation_analysis}\n"
)
PLAYBOOK_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", PLAYBOOK_SYSTEM),
    ("human", PLAYBOOK_HUMAN)
])
