import streamlit as st
from dotenv import load_dotenv
import os
from agents.research_agent import ingest_url_content
from agents.recommendation_agent import check_collateral_relevance
from agents.sales_agent import run_sales_analysis

# Load .env file automatically at startup
load_dotenv()

st.set_page_config(page_title="AI Multi-Provider Sales Assistant", layout="wide")

st.title("💼 Enterprise Multi-Provider Sales Assistant")
st.caption("A clean, modular Capstone architecture running automated environment key loading.")

with st.sidebar:
    st.header("🔑 Credentials Matrix")
    selected_provider = st.selectbox("Select LLM Provider Engine", ["OpenAI", "Groq"])
    st.markdown("---")
    
    # Read key from background vault automatically
    env_key_name = "GROQ_API_KEY" if selected_provider == "Groq" else "OPENAI_API_KEY"
    stored_secret = os.getenv(env_key_name, "")
    
    if stored_secret:
        st.success(f"🔒 Secure key loaded automatically from local .env!")
        api_key_input = stored_secret
    else:
        api_key_input = st.text_input(f"Insert {selected_provider} API Secret Key", type="password")
        
    st.markdown("---")
    st.info(f"Active Framework: LangChain + {selected_provider}")

col_inputs, col_workspace = st.columns([1, 1.2])

with col_inputs:
    st.subheader("🎯 Context Variables Injection")
    with st.form("agent_configuration_form"):
        product_name = st.text_input("Product Name", value="CloudGuard Data Hub")
        product_cat_raw = st.text_input("Product Category", value="Multi-Cloud Zero-Trust Data Architecture")
        value_prop = st.text_input("Value Proposition", value="Unified security policy management over diverse databases.")
        target_customer = st.text_input("Target Decision Maker Title", value="Chief Data Officer")
        
        st.markdown("---")
        company_url = st.text_input("Target Client Domain URL", value="exampleprospect.com")
        competitors_input = st.text_area("Competitors (URLs, Comma Separated)", value="competitorA.com, competitorB.com")
        
        st.markdown("---")
        uploaded_deck = st.file_uploader("Upload Product Overview Document (.txt only)", type=["txt"])
        submit_execution = st.form_submit_button("Generate Strategic Playbook Blueprint", use_container_width=True)

with col_workspace:
    st.subheader("📄 Generated One-Page Sales Brief")
    
    if submit_execution:
        if not api_key_input:
            st.error(f"Authentication Missing: Please configure your {selected_provider} key inside your local .env file.")
        else:
            with st.spinner("Analyzing account records across connected modules..."):
                deck_text = check_collateral_relevance(uploaded_deck)
                scraped_client = ingest_url_content(company_url)
                
                competitor_urls_list = [c.strip() for c in competitors_input.split(",") if c.strip()]
                scraped_competitor_profiles = ""
                for c_url in competitor_urls_list:
                    scraped_competitor_profiles += f"\n--- Vendor Node: {c_url} ---\n" + ingest_url_content(c_url)
                
                try:
                    playbook = run_sales_analysis(
                        api_key=api_key_input, provider=selected_provider, prod_name=product_name, 
                        prod_cat_desc=product_cat_raw, val_prop=value_prop, target_buyer=target_customer, 
                        target_url=company_url, target_context=scraped_client, 
                        competitors_list=competitor_urls_list, competitor_context=scraped_competitor_profiles, 
                        deck_text=deck_text
                    )
                    
                    st.markdown(f"## 📋 STRATEGIC ACCOUNT PLAN: {playbook.target_company_name.upper()}")
                    st.markdown(f"**Deduced Product Category Verticals:** `{playbook.extracted_product_category}`")
                    st.markdown("---")
                    
                    st.markdown("#### 🏢 I. Corporate Strategy & Operational Signals")
                    for sig in playbook.executive_strategy_summary:
                        st.markdown(f"• **[{sig.source_type}]** {sig.finding_summary}")
                        st.caption(f"  *↳ Strategy Tip:* {sig.actionable_relevance}")
                    
                    st.markdown("---")
                    st.markdown("#### ⚔️ II. Competitor Footprint Overlaps")
                    for comp in playbook.competitor_mentions:
                        st.markdown(f"⚠️ **Incumbent Platform:** {comp.competitor_url}")
                        st.markdown(f"  - *Evidence Found:* {comp.footprint_evidence}")
                        st.markdown(f"  - *Displacement Pivot:* **{comp.counter_position}**")
                        
                    st.markdown("---")
                    st.markdown("#### 👥 III. Key Leadership Matrix")
                    for lead in playbook.leadership_roster:
                        st.markdown(f"👤 **{lead.name}** — *{lead.role}*")
                        st.markdown(f"  *Strategic Priority Focus:* {lead.strategic_quote_or_focus}")
                        
                    st.markdown("---")
                    st.markdown("#### 📊 IV. Public Report Analytics (10-K Data)")
                    st.info(playbook.corporate_report_insights)
                    
                    st.markdown("---")
                    st.markdown("#### 🔗 V. Reference Verified Documentation Links")
                    for cite in playbook.article_links:
                        st.markdown(f"- [{cite.title}]({cite.url})")
                        
                except Exception as eval_err:
                    st.error(f"Format Exception Encountered during parsing runtime workflow: {str(eval_err)}")
    else:
        st.info("Awaiting entry coordinates. Provide variables in the panel and click generate.")
