# 💼 Enterprise Multi-Provider Sales Assistant Agent

An AI-driven Multi-Agent Account Discovery engine designed to help B2B sales representatives rapidly ramp up on prospective enterprise clients. The application dynamically ingests public company web endpoints, strips design noise, parses text-based collateral decks, and uses sequential LangChain prompt sequences to synthesize a tactical, one-page sales playbook.

## 🏗️ Project Architecture Layout

The application utilizes a clean, modular, multi-file software engineering structure:

```text
capstone_project/
│
├── main.py                     # Entry point web interface & orchestration
├── agents/
│   ├── __init__.py
│   ├── sales_agent.py          # Primary reasoning agent running sequential LCEL chains & Pydantic structures
│   ├── research_agent.py       # Data grounding scraper engine via BeautifulSoup4
│   └── recommendation_agent.py # Internal collateral parsing utility
│
├── prompts/
│   ├── __init__.py
│   └── prompts.py              # Centralized repository housing isolated prompt templates
│
├── tests/
│   ├── __init__.py
│   └── test_agents.py          # Component validation test harness suite
│
└── README.md                   # System configuration & operational manual
```

## ⚙️ Local Development Installation

Follow these steps to deploy and execute this application repository inside a local Mac OS development workspace environment:

### 1. Repository Setup & Environment Isolation
Initialize your project folder structure and construct an isolated python virtual environment to prevent package conflicts:
```bash
python3 -m venv env
source env/bin/activate
```

### 2. Dependency Resolution
With the virtual environment active `(env)`, install the framework requirements:
```bash
pip install streamlit openai pydantic beautifulsoup4 requests langchain langchain-openai langchain-groq python-dotenv
```

### 3. Injecting Runtime Security Variables
Create a local `.env` file in the root directory to securely house your credentials away from Git source control logs:
```text
OPENAI_API_KEY=your_actual_openai_api_key_here
GROQ_API_KEY=your_actual_groq_api_key_here
```

## 🚀 Running the Orchestration Framework

To launch the multi-agent UI infrastructure loop locally, execute the following command:
```bash
streamlit run main.py
```
Open your standard system browser utility and navigate to `http://localhost:8501`.

## 🛡️ Applied Prompt Engineering & Guardrails

The `prompts/prompts.py` file leverages explicit boundary setting and operational persona alignment. The executing system instructions instruct the language processing tier to enforce rigid use-case restrictions:
1. **Strict Core Mapping:** The agent is locked down via zero-creative-variance configuration layers (`temperature=0.1`) to only process data sets explicitly supporting sales-cycle account synthesis requests.
2. **Defensive Prompt Injection Mitigation:** Any off-topic conversational text entries, queries asking for programming routines, or general trivia elements are safely blocked by systemic guardrail wrappers, enforcing enterprise data privacy.
