# 🧠 Cold Email Generator using LLaMA 3.1, LangChain, ChromaDB & Streamlit

### 🚀 Problem to Solve
Software service companies like **TCS**, **Infosys**, and others work with clients such as **Nike**, **JP Morgan**, and **Kroger** to build software solutions.  
To acquire such projects, sales teams often use **cold emails** to reach potential clients.

This project automates **cold email generation** by extracting job data from client websites and generating personalized emails using **LLaMA 3.1**.

---

## 🧩 Tech Stack

- **LLaMA 3.1 (via Groq Cloud)** — Fast inference using LPUs  
- **LangChain** — Prompt management & LLM orchestration  
- **ChromaDB** — Lightweight vector store for semantic search  
- **Streamlit** — Interactive UI for the app  

---

## 🧭 Workflow Overview

1. **Extract job description** from client career pages using `WebBaseLoader`  
2. **Process text** through LLaMA 3.1 to extract structured info:
   ```json
   {
     "role": "Senior Software Engineer",
     "skills": ["React", "Node.js", "REST APIs"],
     "experience": "2+ years"
   }
