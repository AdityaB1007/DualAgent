TripleAgent

An agentic research assistant that performs autonomous web-based research, drafts detailed answers, and fact-checks them using semantic search and summarization tools — powered by LangGraph, LangChain, FAISS, and OpenAI.

___

Features:

1. Web Research Agent: Searches the web and gathers snippets using Tavily.

2. Answer Drafting Agent: Drafts coherent answers based on gathered research.

3. Fact Checker Agent: Verifies drafted answers using semantic search + summarization.

4. FAISS Vector Store: Stores research snippets for semantic retrieval.

5. LangGraph Pipeline: Declarative multi-agent pipeline.

6. Streamlit Frontend: Easy-to-use interface for entering queries and viewing results.
   
___

Getting Started:

  1. Clone the Repository.
  
  2. Install Dependencies:
    pip install -r requirements.txt
  
  3. Set Up Environment Variables:
   Create a .env file:

     OPENAI_API_KEY=your_openai_key

     TAVILY_API_KEY=your_tavily_key
  
  Make sure you have valid API keys for OpenAI and Tavily.

___

Usage:

  To run in Terminal (CLI mode):
  python main.py
  
  Enter your research question when prompted.
  
  To run in Streamlit Web App:
  streamlit run streamlit_app.py
  
  Access your research assistant through a simple web interface.

___

Example Flow:

1. You enter a research query.
2. The Research Agent collects relevant web snippets.
3. The Answer Agent drafts a detailed answer.
4. The Fact-Checker Agent verifies and refines the answer.
5. You receive the final verified answer along with research snippets and draft!

___

Tech Stack:

  1. LangChain
  2. LangGraph
  3. OpenAI LLMs
  4. Tavily Search
  5. FAISS
  6. Streamlit

___

Known Issues / TODO:

 1. Add Retry mechanism if agent output parsing fails.

 2. Support Gemini, Claude, or other free LLMs.

 3. Enhance Fact-Checking using RAG techniques.

 4. Improve UI (progressive loading of steps).

___

Contributions, issues, and feature requests are welcome!
Open an issue to discuss major changes
Fork the repository and submit a pull request 🚀

___

License
This project is licensed under the MIT License.
