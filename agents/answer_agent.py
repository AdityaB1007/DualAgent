from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from tools.summarizer import summarize_tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI model with API key
openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key:", openai_api_key)

llm = ChatOpenAI(temperature=0.2)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

answer_agent = initialize_agent(
    tools=[summarize_tool],
    llm=llm,
    agent_type="openai-tools",
    memory=memory,
    verbose=True
)

def run_answering(state):
    print("run_answering", state)
    results = state["research_results"]
    answer = answer_agent.run(f"Based on this information, provide a detailed answer: {results}")
    return {"draft_answer": answer}
