from dotenv import load_dotenv
load_dotenv()

from graph.langgraph_flow import compiled_graph

if __name__ == "__main__":
    query = input("Enter your research query: ")
    
    result = compiled_graph.invoke({"query": query})
    print("\n✅ Final Verified Answer:\n", result["verified_answer"])