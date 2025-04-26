from langchain.agents import Tool
from memory.faiss_store import get_faiss_db

def semantic_search(query: str) -> str:
    faiss_db = get_faiss_db()
    docs = faiss_db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])

semantic_search_tool = Tool(
    name="semantic_search",
    func=semantic_search,
    description="Semantic search over research documents."
)
