# 🤖 AI Text Summarizer

An AI-powered web application that instantly summarizes long paragraphs, articles, or any text into short and meaningful summaries. Just paste your text, click summarize, and get a concise summary in seconds — powered by Groq's LLaMA model.

## ✨ Features

- 🚀 Instant AI-powered summarization
- 📝 Clean and simple user interface
- ⚡ Super fast responses using Groq LLaMA model
- 🌐 Accessible from any browser

## 🛠️ Tech Stack

- **Frontend** — HTML, CSS, JavaScript
- **Backend** — Python, Flask
- **AI Model** — Groq API (llama-3.1-8b-instant)

## 📁 Project Structure
```
AI_Text_Summarizer/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── index.html
├── Dockerfile
├── Jenkinsfile
├── .gitignore
└── README.md
```

## 🚀 How to Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/sruthiashok24/AI_Text_Summarizer.git
cd AI_Text_Summarizer
```

**Step 2 — Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**Step 3 — Install dependencies**
```bash
pip install -r backend/requirements.txt
```

**Step 4 — Set up environment variable**

Create a `.env` file in the root folder and add:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key from 👉 https://console.groq.com

**Step 5 — Run the app**
```bash
cd backend
python app.py
```

**Step 6 — Open in browser and enjoy!**

Go to `http://localhost:5000` and experience the power of AI summarization! Simply paste any long article, research paper, news story, or paragraph into the text box and hit the **Summarize** button. Within seconds, our AI will read through your entire content and hand you back a clean, crisp summary - saving you time and helping you understand the core idea without reading through every single line. Whether it's a 10 page article or a long paragraph, just paste it and enjoy understanding the gist instantly! 🚀

## 👥 Team Members

- Prahalya S (23z354)
- Hemashri (23z228)
- Lisha (23z235)
- Sruthi A (23z272)


