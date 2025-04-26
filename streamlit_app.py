# streamlit_app.py
import streamlit as st
from graph.langgraph_flow import compiled_graph

st.set_page_config(page_title="Research AI Assistant", layout="centered")
st.title("🧠 Research AI Assistant")

query = st.text_area("Enter your research question:")

if st.button("Submit Query"):
    if query.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        # Step 1: Show loading state while agents process
        with st.spinner("Gathering research data..."):
            result = compiled_graph.invoke({"query": query})
        
        # Step 2: Display the results progressively
        st.success("✅ Research complete!")

        # Show snippets from research
        st.subheader("🔍 Research Snippets:")
        if "research_results" in result:
            st.write(result["research_results"])  # Research agent output
        else:
            st.warning("No research data found.")
        
        # Show drafted answers from the Answer Agent
        st.subheader("📝 Draft Answer:")
        if "draft_answer" in result:
            st.write(result["draft_answer"])  # Draft answer before fact-checking
        else:
            st.warning("No draft answer available.")
        
        # Step 3: Show final verified answer after fact-checking
        st.subheader("✅ Final Verified Answer:")
        if "verified_answer" in result:
            st.write(result["verified_answer"])  # Final answer after fact-checking
        else:
            st.warning("No verified answer found.")
