import streamlit as st
import requests

# ===================== CONFIG =====================
API_URL = "http://127.0.0.1:5000/api/ask"

st.set_page_config(page_title="Agentic AI Tool", page_icon="🤖", layout="centered")

st.title("🤖 Agentic AI Business System")

# ===================== SESSION MEMORY =====================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ===================== INPUT =====================
user_input = st.text_area("💬 Enter your question:", height=120)

col1, col2 = st.columns(2)

# ===================== ASK BUTTON =====================
if col1.button("🚀 Ask AI"):
    if not user_input.strip():
        st.warning("Please enter a question!")
    else:
        with st.spinner("Thinking... 🤖"):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "agent": None,   # 🔥 auto routing
                        "question": user_input
                    }
                )

                data = response.json()
                answer = data.get("response", "Error occurred")

                # save to history
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("AI", answer))

            except Exception as e:
                st.error(f"Error: {e}")

# ===================== CLEAR BUTTON =====================
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
