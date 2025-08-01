﻿ # 🧠 AI Analyst Junior

A lightweight AI-powered data analyst tool built with **Flask**, **LangChain**, and **Google Gemini API**.  
Upload a CSV file and ask questions — the app will answer intelligently using LLMs!

---

## 🚀 Features

- 📁 Upload CSV and chat with your data
- 🤖 Powered by Gemini + LangChain agents
- 🧮 Supports analysis, summaries, and basic calculations
- 🧼 Clean UI using HTML + Bootstrap
- 🔐 Error handling and security-aware prompts

---

## 🛠️ Tech Stack

- Python 3.11+
- Flask
- LangChain
- Google Generative AI (Gemini)
- Pandas
- HTML + CSS (Bootstrap)
- OpenAI-compatible agent setup

---

## 📦 Installation

```bash
git clone https://github.com/Jawaharsrinath2/AI_Analyst_jr.git
cd AI_Analyst_jr
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt

## to run
python app.py


AI_Analyst_jr/
├── app.py
├── templates/
│   ├── chat.html
│   └── result.html
├── static/
│   └── (optional styles)
├── requirements.txt
└── README.md


🛡️ Security Notes
This project disables dangerous code execution unless explicitly enabled.
Refer to LangChain security guidelines:
https://python.langchain.com/docs/security/

BUILD BY
JAWAHARSRINATH NATARAJAN

