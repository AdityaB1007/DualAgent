from langgraph.graph import StateGraph
from agents.research_agent import run_research
from agents.answer_agent import run_answering
from agents.fact_checker_agent import run_fact_checker

class ResearchState(dict):
    query: str
    research_results: str
    draft_answer: str
    verified_answer: str

graph = StateGraph(ResearchState)
graph.add_node("research", run_research)
graph.add_node("answer", run_answering)  # Runs after research
graph.add_node("fact_checker", run_fact_checker)  # Runs after answering

graph.set_entry_point("research")
graph.add_edge("research", "answer")  # Pass state from research to answer
graph.add_edge("answer", "fact_checker")  # Pass state from answer to fact_checker
graph.set_finish_point("fact_checker")

compiled_graph = graph.compile()