import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/api/stream"

st.title("🤖 Agentic AI (Streaming)")

user_input = st.text_area("Ask something:")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Ask AI"):
    if not user_input.strip():
        st.warning("Enter question")
    else:
        response_placeholder = st.empty()
        full_response = ""

        try:
            with requests.post(API_URL, json={"question": user_input}, stream=True) as res:
                for chunk in res.iter_content(chunk_size=10):
                    if chunk:
                        text = chunk.decode("utf-8")
                        full_response += text
                        response_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"Error: {e}")
# ===================== CLEAR BUTTON =====================
col1, col2 = st.columns(2)
if col2.button("🧹 Clear Chat"):
    st.session_state.chat_history = []

# ===================== CHAT DISPLAY =====================
st.markdown("## 💬 Conversation")

for role, text in st.session_state.chat_history[::-1]:
    if role == "You":
        st.markdown(f"**🧑 {role}:** {text}")
    else:
        st.markdown(f"**🤖 {role}:** {text}")

# ===================== DOWNLOAD =====================
if st.session_state.chat_history:
    full_text = "\n\n".join([f"{role}: {msg}" for role, msg in st.session_state.chat_history])
    st.download_button("⬇️ Download Chat", full_text, file_name="chat.txt")
