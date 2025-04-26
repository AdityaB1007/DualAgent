from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults
from memory.faiss_store import add_to_faiss
import os
from dotenv import load_dotenv
from langchain.schema import Document

# Load environment variables
load_dotenv()

# Get OpenAI API key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment variables.")

# Initialize ChatOpenAI
llm = ChatOpenAI(api_key=openai_api_key, temperature=0)

# Add Tavily search tool
search_tool = TavilySearchResults(max_results=5)

# Initialize the research agent
research_agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent_type="zero-shot-react-description",
    handle_parsing_errors=True,
    verbose=True
)

# Research runner function for LangGraph
def run_research(state):
    query = state["query"]
    result = research_agent.run(query)
    
    # Create Document properly and pass text only to FAISS
    doc = Document(page_content=result, metadata={"source": "agent"})
    add_to_faiss(doc)
    
    return {"query": query, "research_results": result}

