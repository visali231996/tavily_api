
import streamlit as st
import random
import time
from example import get_response
from typing import List
from io import BytesIO

st.title("Latest News Updates")

def compress_query(text: str) -> str:
    """
    Shortens long inputs so Tavily does not throw
    'Query too long: Max query length = 400 characters'
    """
    if len(text) <= 300:
        return text
    
    # Keep only the latest user query part (best for news/search)
    parts = text.split("latest query:")
    if len(parts) > 1:
        latest = parts[-1].strip()
        return latest[:300]  # Hard limit
    
    return text[:300]
    
# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)




# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history: List[str] = [] # type: ignore

def build_chat_template(history: List[str], latest_query: str, max_turns: int = 5) -> str:
    pruned = history[-max_turns:] if len(history) > max_turns else history
    prev = "\n".join(pruned) if pruned else "(none)"
    return f"Previous conversation: {prev}\nlatest query:{latest_query}"


    
    # ---- Show prior messages (best-effort split for display only) ----
for turn in st.session_state.history:
    # turn looks like: "User: ...\nAgent: ..."
    parts = turn.split("\nAgent:", 1)
    user_line = parts[0].removeprefix("User: ").strip()
    with st.chat_message("user"):
        st.markdown(user_line)
    if len(parts) == 2:
        agent_line = parts[1].strip()
        with st.chat_message("assistant"):
            st.markdown(agent_line)
    

MAX_TURNS_MEMORY = 5
MAX_MEMORY_CHARS = 2000

if query := st.chat_input("How can I help you?"):
    # build memory_text from last N turns (most recent first)
    pruned = st.session_state.history[-MAX_TURNS_MEMORY:]
    memory_text = "\n".join(pruned)
    # guard memory length
    if len(memory_text) > MAX_MEMORY_CHARS:
        memory_text = memory_text[-MAX_MEMORY_CHARS:]

    try:
        response = get_response(query, memory_text)
    except Exception as e:
        response = f"[Error contacting model] {e}"

    st.chat_message("user").markdown(query)
    st.chat_message("assistant").markdown(response)

    # store turn for future memory
    st.session_state.history.append(f"User: {query}\nAgent: {response}")
    # keep history length reasonable
    st.session_state.history = st.session_state.history[-(MAX_TURNS_MEMORY * 2):]


