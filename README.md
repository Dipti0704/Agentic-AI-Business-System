# 🤖 Agentic AI Business System

A production-ready **Multi-Agent AI Platform** powered by **Ollama (Local LLM)** that helps businesses automate **Sales, Marketing, Copywriting, and Analytics**.

---

## 🚀 What is this?

This is not just a chatbot ❌  
This is a **complete business AI system** ✅  

👉 Users interact through a UI  
👉 System routes query to the correct AI agent  
👉 Each agent gives domain-specific intelligent output  

---

## 🧠 Agents in the System

| Agent        | Purpose |
|-------------|--------|
| 🛒 Sales Agent | Increase revenue, conversions |
| 📢 Marketing Agent | Ads, SEO, campaigns |
| ✍️ Copywriting Agent | Ad copy, content |
| 📊 Analytics Agent | Reports, insights |

---

## 🏗️ Architecture (Simple Flow)

User → Frontend → Backend API → Agent Manager → Agent → Ollama → Response → UI  

---

## 📂 Project Structure

agentic-ai-final/
│
├── agents/
│ ├── sales_agent.py
│ ├── marketing_agent.py
│ ├── copywriting_agent.py
│ └── analytics_agent.py
│
├── prompts/
│ ├── sales_prompt.txt
│ ├── marketing_prompt.txt
│ ├── copywriting_prompt.txt
│ └── analytics_prompt.txt
│
├── core/
│ ├── agent_base.py
│ ├── agent_manager.py
│ └── utils.py
│
├── backend/
│ ├── app.py
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md


---

## ⚙️ Setup (Step-by-Step)

### 1. Install dependencies
pip install -r backend/requirements.txt


---

### 2. Install Ollama

👉 https://ollama.com

---

### 3. Pull model
ollama pull llama3

(or faster)

ollama pull phi3


---

### 4. Run backend
python -m backend.app


👉 Runs at:  
http://127.0.0.1:5000

---

### 5. Open UI

👉 http://127.0.0.1:5000  

---

## 💡 Example Usage

### Sales Question:
I have a medical shop. How can I increase sales?

### Output:
- Promotions strategy  
- Customer engagement ideas  
- Online marketing plan  

---

## 🔥 Features

- Multi-Agent AI System  
- Local LLM (No API cost)  
- Clean UI  
- Modular backend  
- Real-time AI responses  
- Business-focused outputs  

---

## ⚡ Tech Stack

- Python (Flask)
- HTML, CSS, JavaScript
- Ollama (LLM)

---

## 🚀 Future Improvements

- Memory (chat history)  
- RAG (document-based AI)  
- Dashboard UI  
- Multi-agent collaboration  

---

## 👨‍💻 Author

Adhav  
AI Developer 🚀  

---

## ⭐ Support

If you like this project:
- Star ⭐  
- Share 🔗  
- Connect 🤝  

---

## 🔥 Tagline

"This is not a chatbot. This is a Business AI System."