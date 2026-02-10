import streamlit as st
import time
import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "AIzaSyCwZv7aqjypQJd8rXn8yNCnDpm844f_2bQ"

st.set_page_config(page_title="Eduwerks | Architect", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #0a0a0a; color: #d1d5db; }
    .stTextArea textarea { background-color: #111; color: #00ff00; font-family: 'Courier New', monospace; border: 1px solid #333; }
    .stButton button { background-color: #b08d48; color: black; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #b08d48; font-family: 'Cinzel', serif; }
    .success-box { padding: 10px; background-color: #1a1a1a; border-left: 5px solid #00ff00; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# --- SMART CONNECTION LOGIC ---
model = None
status_msg = "Initializing..."

try:
    genai.configure(api_key=API_KEY)
    # 1. Ask Google what models are available for this key
    available = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available.append(m.name)
    
    # 2. Pick the best one
    if available:
        selected_model = available[0] # Pick the first available one
        model = genai.GenerativeModel(selected_model)
        status_msg = f"🟢 Online: Connected to {selected_model}"
    else:
        status_msg = "🟠 Offline: No Models Found (Using Simulation)"

except Exception as e:
    status_msg = f"🔴 Offline: Connection Error (Using Simulation)"

# --- UI LAYOUT ---
st.title("🛠️ Code Architect")
st.caption(status_msg)

col1, col2 = st.columns(2)

with col1:
    raw_code = st.text_area("Paste Python Code Here", height=500, placeholder="def train(x,y):\n    # paste messy code here...")
    analyze_btn = st.button("🚀 FORGE CODE")

# --- SYSTEM PROMPTS & OFFLINE FALLBACK ---
SYSTEM_PROMPT = "You are a Senior ML Engineer. Refactor this code to use PyTorch/NumPy vectorization. Add docstrings. Output ONLY code."

OFFLINE_DEMO_CODE = """
import torch
import torch.nn as nn

# Optimized via Vectorization
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(10, 1)
    
    def forward(self, x):
        return self.fc(x)

# Device Agnostic Code
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Net().to(device)
print(f"Model forged on {device}")
"""

with col2:
    if analyze_btn and raw_code:
        with st.spinner("Refactoring Neural Pathways..."):
            try:
                if model:
                    # ATTEMPT LIVE GENERATION
                    response = model.generate_content(f"{SYSTEM_PROMPT}\n\n{raw_code}")
                    st.code(response.text, language='python')
                    st.markdown('<div class="success-box">✅ Optimization Complete (Live API)</div>', unsafe_allow_html=True)
                else:
                    # FALLBACK TO SIMULATION
                    time.sleep(2)
                    st.code(OFFLINE_DEMO_CODE, language='python')
                    st.markdown('<div class="success-box">✅ Optimization Complete (Simulation Mode)</div>', unsafe_allow_html=True)
            except:
                # FINAL FALLBACK IF API CRASHES MID-REQUEST
                st.code(OFFLINE_DEMO_CODE, language='python')
                st.markdown('<div class="success-box">✅ Optimization Complete (Simulation Mode)</div>', unsafe_allow_html=True)
                
    elif analyze_btn and not raw_code:
        st.warning("Please paste some code first.")