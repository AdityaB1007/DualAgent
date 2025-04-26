from langchain.chains.summarize import load_summarize_chain
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI model
llm = ChatOpenAI(temperature=0.2)

# Load summarization chain
summarization_chain = load_summarize_chain(llm, chain_type="map_reduce")

def summarize_text(text: str) -> str:
    # Wrap the text in a Document object
    docs = [Document(page_content=text)]
    return summarization_chain.run(docs)

summarize_tool = Tool(
    name="summarize",
    func=summarize_text,
    description="Summarizes long chunks of research text."
)
