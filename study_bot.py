import streamlit as st
import time
import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "AIzaSyCwZv7aqjypQJd8rXn8yNCnDpm844f_2bQ"

st.set_page_config(page_title="Eduwerks | Scribe", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #0f1115; color: #d1d5db; }
    .chat-bubble { padding: 15px; border-radius: 10px; margin-bottom: 10px; max-width: 80%; }
    .user-bubble { background: #1a1a1a; border-left: 4px solid #b08d48; margin-left: auto; text-align: right; }
    .bot-bubble { background: #0a0a0a; border-left: 4px solid #2e7d32; margin-right: auto; }
    .stTextInput input { background-color: #1a1a1a; color: white; border: 1px solid #333; }
    h1 { color: #2e7d32; font-family: 'Cinzel', serif; }
</style>
""", unsafe_allow_html=True)

# --- SMART CONNECTION LOGIC ---
model = None
status_msg = "Initializing..."

try:
    genai.configure(api_key=API_KEY)
    available = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available.append(m.name)
            
    if available:
        selected_model = available[0]
        model = genai.GenerativeModel(selected_model)
        status_msg = f"🟢 Online: {selected_model}"
    else:
        status_msg = "🟠 Offline (Simulation)"
except:
    status_msg = "🔴 Offline (Simulation)"

# --- UI LAYOUT ---
st.title("📜 The Study Scribe")
st.caption(status_msg)

if "scribe_history" not in st.session_state:
    st.session_state.scribe_history = []

# History
for msg in st.session_state.scribe_history:
    role = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    st.markdown(f"<div class='chat-bubble {role}'>{msg['content']}</div>", unsafe_allow_html=True)

# --- OFFLINE KNOWLEDGE BASE ---
OFFLINE_DATA = {
    "default": "I am the Study Scribe. I can create Schedules, Explain Topics, or provide Motivation.",
    "schedule": "**Study Decree:**\n- 09:00 AM: Deep Learning Theory\n- 12:00 PM: PyTorch Labs\n- 04:00 PM: Project Work\n*Consistency is key.*",
    "explain": "**Concept Breakdown:**\nImagine a Neural Network as a committee of decision makers. Each layer passes a vote to the next, refining the decision until the final output is reached.",
    "motivation": "**Maester's Wisdom:**\n'The climb is all there is.' Do not fear the error function. Embrace the gradient."
}

def get_offline_response(txt):
    txt = txt.lower()
    if "schedule" in txt: return OFFLINE_DATA["schedule"]
    if "explain" in txt or "what" in txt: return OFFLINE_DATA["explain"]
    if "motiv" in txt: return OFFLINE_DATA["motivation"]
    return OFFLINE_DATA["default"]

# Input
if prompt := st.chat_input("Ex: Create a schedule..."):
    st.markdown(f"<div class='chat-bubble user-bubble'>{prompt}</div>", unsafe_allow_html=True)
    st.session_state.scribe_history.append({"role": "user", "content": prompt})

    with st.spinner("Writing scroll..."):
        response_text = ""
        try:
            if model:
                # TRY API
                full_prompt = f"You are an academic assistant. Answer this briefly: {prompt}"
                response = model.generate_content(full_prompt)
                response_text = response.text
            else:
                # FALLBACK
                time.sleep(1)
                response_text = get_offline_response(prompt)
        except:
            # SAFETY CATCH
            response_text = get_offline_response(prompt)

        st.markdown(f"<div class='chat-bubble bot-bubble'>{response_text}</div>", unsafe_allow_html=True)
        st.session_state.scribe_history.append({"role": "assistant", "content": response_text})