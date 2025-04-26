from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from tools.semantic_search import semantic_search_tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI model with API key
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0.2)

fact_checker_agent = initialize_agent(
    tools=[semantic_search_tool],
    llm=llm,
    agent_type="openai-tools",
    verbose=True
)

def run_fact_checker(state):
    print("run_fact_checker_",state)
    answer = state["draft_answer"]
    result = fact_checker_agent.run(
        f"Check the following answer for factual accuracy using semantic search: {answer}"
    )
    return {"verified_answer": result}
