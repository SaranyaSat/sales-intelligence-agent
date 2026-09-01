from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import List
from prompts.prompts import (
    STRATEGY_PROMPT_TEMPLATE, 
    RESEARCH_PROMPT_TEMPLATE, 
    RECOMMENDATION_PROMPT_TEMPLATE,
    PLAYBOOK_PROMPT_TEMPLATE
)

# =====================================================================
# NATIVE PYTHON TOOLS (Instructor's Step 12 Blueprint)
# =====================================================================
@tool
def verify_solution_inventory(solution_module_name: str) -> str:
    """Check whether our product offering module is currently available to pitch."""
    return f"[AGENT TOOL RUNNED]: Offering module '{solution_module_name}' is fully deployed and available for allocation."

# =====================================================================
# STRUCTURED PYDANTIC LAYOUT SCHEMAS (Instructor's Step 11 Blueprint)
# =====================================================================
class StrategicSignal(BaseModel):
    source_type: str = Field(description="Signal origin tracking category entry.")
    finding_summary: str = Field(description="Synthesis of corporate activity or technology configuration.")
    actionable_relevance: str = Field(description="How the rep can frame this point to position their solution.")

class CompetitorOverlap(BaseModel):
    competitor_url: str = Field(description="The website URL of the target rival.")
    footprint_evidence: str = Field(description="Mentions or structural indicators showing alternative software presence.")
    counter_position: str = Field(description="The exact tactical angle to use to win against this competitor.")

class LeaderInsight(BaseModel):
    name: str = Field(description="Name of the executive leader.")
    role: str = Field(description="Exact title, e.g., Chief Data Officer, VP of Engineering.")
    strategic_quote_or_focus: str = Field(description="Summary of recent public commentary or target authority spheres.")

class Citation(BaseModel):
    title: str = Field(description="Description of the referenced webpage or document.")
    url: str = Field(description="Direct web link verified during extraction.")

class PerScholasSalesPlaybook(BaseModel):
    target_company_name: str = Field(description="The official name of the prospective client.")
    extracted_product_category: str = Field(description="The short category classification derived from the user's description.")
    executive_strategy_summary: List[StrategicSignal] = Field(description="Dynamic indicators built from public activities.")
    competitor_mentions: List[CompetitorOverlap] = Field(description="Analysis mapping rival footprints.")
    leadership_roster: List[LeaderInsight] = Field(description="Key stakeholder tracking list.")
    corporate_report_insights: str = Field(description="Deep context mined from financial statements or profile documentation.")
    article_links: List[Citation] = Field(description="Clean references linking back to verification materials.")

# =====================================================================
# MULTI-PROVIDER SEQUENTIAL PROCESSING ENGINE (Instructor's Steps 8-10)
# =====================================================================
def run_sales_analysis(
    api_key: str, provider: str, prod_name: str, prod_cat_desc: str, val_prop: str, 
    target_buyer: str, target_url: str, target_context: str, 
    competitors_list: List[str], competitor_context: str, deck_text: str
) -> PerScholasSalesPlaybook:
    
    # 1. Model Switching Layer (Swapping Providers easily)
    if provider == "Groq":
        base_llm = ChatGroq(model="qwen-2.5-32b", temperature=0, groq_api_key=api_key)
    else:
        base_llm = ChatOpenAI(model="gpt-4o", temperature=0.1, openai_api_key=api_key)
        
    # Bind our Python tool to the model engine
    llm_with_tools = base_llm.bind_tools([verify_solution_inventory])
    text_parser = StrOutputParser()
    
    # 2. Build Sequential LCEL Chains using the (|) operator
    strategy_chain = STRATEGY_PROMPT_TEMPLATE | base_llm | text_parser
    research_chain = RESEARCH_PROMPT_TEMPLATE | base_llm | text_parser
    recommendation_chain = RECOMMENDATION_PROMPT_TEMPLATE | llm_with_tools | text_parser
    
    # Final layer generates the structured Pydantic record object
    structured_llm = base_llm.with_structured_output(PerScholasSalesPlaybook)
    playbook_chain = PLAYBOOK_PROMPT_TEMPLATE | structured_llm
    
    # 3. Information Passing Workflow (Passing Output Between Chains)
    strategy_output = strategy_chain.invoke({
        "prod_name": prod_name,
        "target_buyer": target_buyer,
        "target_context": target_context
    })
    
    competitors_str = ", ".join(competitors_list)
    research_output = research_chain.invoke({
        "competitors_str": competitors_str,
        "strategy_analysis": strategy_output,
        "competitor_context": competitor_context
    })
    
    recommendation_output = recommendation_chain.invoke({
        "strategy_analysis": strategy_output,
        "research_analysis": research_output,
        "deck_text": deck_text
    })
    
    final_playbook_blueprint = playbook_chain.invoke({
        "target_company_url": target_url,
        "strategy_analysis": strategy_output,
        "research_analysis": research_output,
        "recommendation_analysis": recommendation_output
    })
    
    return final_playbook_blueprint
