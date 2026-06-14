import streamlit as st
import google.generativeai as genai
from datetime import datetime

# Gemini API Key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# Page Settings
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📚 AI Study Assistant")

    st.write("### Developer")
    st.write("Samrudhi Kulkarni")

    st.write("---")

    st.write("### Technologies")
    st.write("✅ Python")
    st.write("✅ Streamlit")
    st.write("✅ Gemini AI")

    st.write("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main Page
st.title("📚 AI Study Assistant")
st.subheader("Developed by Samrudhi Kulkarni")

st.write(
    "Ask questions about Python, DBMS, OOP, Machine Learning, Communication Systems, MPSC and more."
)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
user_input = st.chat_input("Ask a question...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    try:
        prompt = f"""
You are an expert study assistant.

Rules:
- Explain concepts in simple language.
- Give examples whenever possible.
- Answer clearly and accurately.
- Help students learn effectively.

Question:
{user_input}
"""

        response = model.generate_content(prompt)
        answer = response.text

    except Exception as e:
        answer = f"Error: {e}"

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)

    # Save Chat History
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(
            f"\n[{datetime.now()}]\n"
            f"User: {user_input}\n"
            f"Assistant: {answer}\n"
            f"{'-'*50}\n"
        )