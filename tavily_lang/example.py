from langgraph.graph import StateGraph, END
import tavily
from langchain_groq import ChatGroq
from IPython.display import display_markdown
import os
from dotenv import load_dotenv
load_dotenv()
from tavily import TavilyClient
from typing import TypedDict

# --- 1) Init Tavily + LLM ---
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-20b"
)

# --- 2) Safe Tavily wrapper (prevents 400-char errors) ---
def safe_tavily_search(query: str, max_length: int = 400, **kwargs):
    if len(query) > max_length:
        print(f"⚠️ Tavily query too long ({len(query)}). Truncating to {max_length}.")
        query = query[:max_length]
    try:
        return tavily.search(query=query, **kwargs)
    except Exception as e:
        print("❌ Tavily search error:", e)
        return {"results": []}

# --- 3) Agent state (now includes memory) ---
class AgentState(TypedDict):
    question: str
    memory: str           # <-- additional field for history / context
    search_results: dict
    summarized_answer: str

# --- 4) Node 1: Tavily Search (references only) ---
def search_web(state: AgentState):
    # IMPORTANT: only use state["question"] for Tavily (no memory)
    print(f"🔍 Searching (Tavily) for: {state['question']!r}")
    search_results = safe_tavily_search(
        query=state["question"],
        max_results=5,
        include_answer=False
    )
    return {"search_results": search_results}

# --- 5) Node 2: Summarize using LLM (this node receives memory separately) ---
def summarize_with_llm(state: AgentState):
    print("🧠 Summarizing references with memory...")

    results = state["search_results"].get("results", [])
    if not results:
        return {"summarized_answer": "⚠️ No relevant search results found."}

    snippets = "\n\n".join(
        f"{item.get('title','(no title)')} — {item.get('content','')}" for item in results
    )

    # incorporate memory if available (but keep it concise)
    memory_text = state.get("memory", "")
    if len(memory_text) > 2000:
        memory_text = memory_text[-2000:]  # keep last 2000 characters

    prompt = f"""
You are a helpful AI assistant. Use the user's recent conversation (memory) and the web results below to answer the user.
Return a concise, factual answer (2-3 paragraphs) in json format .

User conversation (memory):
{memory_text}

User question:
{state['question']}

Information from web results:
{snippets}
"""

    llm_response = llm.invoke(prompt)
    sources = [f"- {r.get('title','(no title)')}: {r.get('url','(no url)')}" for r in results]
    final_answer = f"{llm_response.content}\n\nSources:\n" + "\n".join(sources)
    return {"summarized_answer": final_answer}

# --- 6) Build workflow ---
def create_agent():
    workflow = StateGraph(AgentState)
    workflow.add_node("search", search_web)
    workflow.add_node("summarize", summarize_with_llm)
    workflow.set_entry_point("search")
    workflow.add_edge("search", "summarize")
    workflow.add_edge("summarize", END)
    return workflow.compile()

# --- 7) get_response now accepts memory and passes it into the agent state ---
def get_response(query: str, memory: str = "") -> str:
    agent = create_agent()
    # Pass BOTH the question and the memory into the agent state.
    # The search node will only use the question; the summarize node will use memory.
    input_state = {"question": query, "memory": memory}
    output = agent.invoke(input_state)

    print("\n🧩 Agent output keys:", output.keys())
    display_markdown(output.get("summarized_answer", "⚠️ No summary generated."))
    return output.get("summarized_answer", "⚠️ No summary generated.")
