from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model = OpenAIEmbeddings()
faiss_db = None  # Global FAISS index

def add_to_faiss(document: Document):
    global faiss_db
    if not isinstance(document, Document):
        raise TypeError("Expected a Document object")
    
    if faiss_db is None:
        faiss_db = FAISS.from_documents([document], embedding_model)
    else:
        faiss_db.add_documents([document])

def get_faiss_db():
    global faiss_db
    if faiss_db is None:
        raise ValueError("FAISS DB is not initialized. Add some documents first.")
    return faiss_db
