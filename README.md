<b>Latest News Bot using Tavily:</b><br>
Gives latest news updates and summarizes the outcome using langgraph.<br>
Tavily API is used to extract latest news updates, unlike OpenAI and Groq API which provide already stored information.<br>
<br>
<b><u>Features</u></b><br>
<b>Frontend (Streamlit Client)</b><br>
- Session-based conversation management<br>
- Clean UI with custom styling<br>
- User and assistant avatars<br>
- Built-in suggestion prompts for quick queries<br>
- Support for Markdown and PDF transcript export<br>
- Automatic session identification<br>
- Secure environment variable usage<br>
<br>
<b>Backend (Expected Components)</b><br>
While the backend may be kept in a separate service, the client assumes that the backend provides:<br>
- A <code>/chat</code> POST endpoint<br>
- Retrieval-Augmented Generation logic<br>
- Optional external news or web search (Tavily or other services)<br>
- Citations with title, URL, and snippet fields<br>
<br>
<b><u>Project Structure:</u></b><br>
<pre>
tavily_lang/
├── __pycache__/
├── .ven/
├── .env
├── stream.py
├── ex.ipynb
├── example.py
└── tavily_api.py
</pre>
<br>
<b><u>Requirements</u></b><br>
<b>Python Version</b><br>
Python 3.9 or later is recommended.<br>
<br>
<b>Install with Poetry</b><br>
<pre>poetry install</pre>
<b>Install with pip</b><br>
<pre>pip install -r requirements.txt</pre>
<br>
<b><u>Environment Variables</u></b><br>
Create a <code>.env</code> file in the project root:<br>
<pre>
NEWS_AGENT_API_URL=http://127.0.0.1:8000/chat
OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
</pre>
<i>The .env file contains sensitive information and must not be committed to GitHub.</i><br>
<br>
<b><u>Running the Application</u></b><br>
- For streaming on Streamlit UI:<br>
<pre>streamlit run stream.py</pre>
- For running as API:<br>
<pre>
python -m venv venv
venv\scripts\activate
uvicorn tavily_api:app --reload
</pre>
<br>
<b><u>Expected Output Format:</u></b><br>
The output will be in JSON format.<br>
It contains the five latest news items related to the query given by the user.<br>
At the end, it contains sources related to the news and also some URLs.<br>
