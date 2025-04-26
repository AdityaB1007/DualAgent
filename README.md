Research AI Assistant
An agentic research assistant that performs autonomous web-based research, drafts detailed answers, and fact-checks them using semantic search and summarization tools — powered by LangGraph, LangChain, FAISS, and OpenAI.

Features
1. Web Research Agent: Searches the web and gathers snippets using Tavily.

2. Answer Drafting Agent: Drafts coherent answers based on gathered research.

3. Fact Checker Agent: Verifies drafted answers using semantic search + summarization.

4. FAISS Vector Store: Stores research snippets for semantic retrieval.

5. LangGraph Pipeline: Declarative multi-agent pipeline.

6. Streamlit Frontend: Easy-to-use interface for entering queries and viewing results.

Project Structure
research-ai-assistant/
│
├── agents/
│   ├── research_agent.py
│   ├── answer_agent.py
│   └── fact_checker_agent.py
│
├── memory/
│   ├── faiss_store.py
│   └── semantic_search.py
│
├── tools/
│   └── summarizer.py
│
├── graph/
│   └── langgraph_flow.py
│
├── streamlit_app.py
├── main.py
├── .env
└── requirements.txt


Getting Started
1. Clone the Repository.

2. Install Dependencies:
  pip install -r requirements.txt

3. Set Up Environment Variables:
  Create a .env file:
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key

Make sure you have valid API keys for OpenAI and Tavily.

Usage
To run in Terminal (CLI mode):
python main.py

Enter your research question when prompted.

To run in Streamlit Web App:
streamlit run streamlit_app.py

Access your research assistant through a simple web interface.

Example Flow:

You enter a research query.

The Research Agent collects relevant web snippets.

The Answer Agent drafts a detailed answer.

The Fact-Checker Agent verifies and refines the answer.

You receive the final verified answer along with research snippets and draft!

Tech Stack

LangChain

LangGraph

OpenAI LLMs

Tavily Search

FAISS

Streamlit


Known Issues / TODO:

 Add Retry mechanism if agent output parsing fails.

 Support Gemini, Claude, or other free LLMs.

 Enhance Fact-Checking using RAG techniques.

 Improve UI (progressive loading of steps).


Contribution

Contributions, issues, and feature requests are welcome!

Open an issue to discuss major changes

Fork the repository and submit a pull request 🚀

License
This project is licensed under the MIT License.
