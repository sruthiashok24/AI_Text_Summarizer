# ⚡ NeuralSum — AI Text Toolkit
> *Summarize · Analyze · Compare · Extract — at warp speed*

An AI-powered web application that instantly summarizes, analyzes, and compares text in multiple languages and styles — powered by **Groq's LLaMA 3** model. Paste any article, research paper, or paragraph and get a crisp, intelligent summary in seconds.

![NeuralSum](https://img.shields.io/badge/Powered%20By-Groq%20%2B%20LLaMA%203-00e5ff?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask)
![AWS](https://img.shields.io/badge/AWS-EC2%20Deployed-FF9900?style=for-the-badge&logo=amazonaws)

---

## 🌐 Live Application

| Platform | URL |
|----------|-----|
| 🖥️ AWS EC2 (Live) | http://13.201.28.34:5000 |
| 🐳 DockerHub Image | https://hub.docker.com/r/sruthi23z272/ai-text-summarizer |

---

## ✨ Features

### 🔧 Core Functionality
- **✅ Summarize** — Instantly condense long text into short, meaningful summaries
- **✅ Analyze** — Deep analysis of tone, sentiment, and key themes
- **✅ Compare** — Compare two pieces of text side by side
- **✅ History** — View all your previous summarizations

### 🎨 Summary Styles
Choose how you want your summary:
- **Concise** — Short and to the point
- **Detailed** — In-depth explanation
- **Bullet Points** — Clean listed format
- **ELI5** — Explain Like I'm 5 (simple language)
- **Tweet-size** — 280 characters or less

### 🌍 Output Languages
Get your summary in:
- 🇬🇧 English
- 🇮🇳 Tamil
- 🇮🇳 Hindi
- 🇫🇷 French
- 🇪🇸 Spanish

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python 3.11, Flask |
| AI Model | Groq API — llama-3.1-8b-instant (LLaMA 3) |
| Containerization | Docker |
| CI/CD | Jenkins + GitHub Actions |
| Cloud | AWS EC2 (Amazon Linux 2023) |
| Registry | DockerHub |

---

## 📁 Project Structure

```
AI_Text_Summarizer/
├── .github/
│   └── workflows/
│       └── pipeline.yml        ← GitHub Actions (6 stages)
├── backend/
│   ├── app.py                  ← Flask API server
│   └── requirements.txt        ← Python dependencies
├── frontend/
│   └── index.html              ← NeuralSum UI
├── Dockerfile                  ← Container build instructions
├── Jenkinsfile                 ← Jenkins CI/CD pipeline (4 stages)
├── .gitignore
└── README.md
```

---

## 🚀 How to Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/sruthiashok24/AI_Text_Summarizer.git
cd AI_Text_Summarizer
```

**Step 2 — Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**Step 3 — Install dependencies**
```bash
pip install -r backend/requirements.txt
```

**Step 4 — Set up environment variable**

Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free API key from 👉 https://console.groq.com

**Step 5 — Run the app**
```bash
cd backend
python app.py
```

**Step 6 — Open in browser**
```
http://localhost:5000
```

---

## 🐳 Run via Docker

**Pull and run the image directly from DockerHub:**
```bash
docker pull sruthi23z272/ai-text-summarizer:latest



docker run -d \
  -p 5000:5000 \
  -e GROQ_API_KEY=your_groq_api_key_here \
  sruthi23z272/ai-text-summarizer:latest
```

Then open: **http://localhost:5000** 🎉

---

## ⚙️ CI/CD Pipeline

### 🔵 Jenkins Pipeline (Jenkinsfile) — 4 Stages

```
Stage 1 → Clone        : Pull code from GitHub main branch
Stage 2 → Build        : Build Docker image from Dockerfile
Stage 3 → Push         : Push image to DockerHub (sruthi23z272/ai-text-summarizer)
Stage 4 → Deploy       : SSH into AWS EC2, pull image, run container on port 5000
```

### 🟣 GitHub Actions (.github/workflows/pipeline.yml) — 6 Stages

```
Stage 1 → Checkout & Validation     : Clone repo, validate required files exist
Stage 2 → Install & Build           : Set up Python, install dependencies, verify imports
Stage 3 → Code Quality & Security   : Flake8 linting, Bandit security scan, Safety CVE scan
Stage 4 → Build Docker Image        : Build and smoke test Docker image
Stage 5 → Push to DockerHub         : Push image with :latest and commit SHA tags
Stage 6 → Pipeline Summary          : Full report of all stage results
```

---

## ☁️ AWS EC2 Deployment

| Detail | Value |
|--------|-------|
| Cloud Provider | AWS |
| Instance Type | t2.micro (Free Tier) |
| OS | Amazon Linux 2023 |
| Public IP | 13.201.28.34 |
| Port | 5000 |
| Docker Version | 25.0.14 |
| Container Name | summarizer |
| Live URL | http://13.201.28.34:5000 |

**Deployment command used on EC2:**
```bash
docker pull sruthi23z272/ai-text-summarizer:latest
docker run -d --name summarizer -p 5000:5000 \
  -e GROQ_API_KEY=your_key \
  sruthi23z272/ai-text-summarizer:latest
```

---

## 📋 User Stories
Many user stories were raised as GitHub Issues at the start of the project, covering all major features of the application — from text summarization and multi-language output to Docker containerization and EC2 cloud deployment. Each user story was worked on in a dedicated branch and merged into main via Pull Requests. All issues have been successfully resolved and closed, reflecting a complete agile-style development lifecycle from requirement to deployment.

## 👥 Team Members

| Name | Roll Number |
|------|------------|
| Prahalya S | 23z354 |
| Hemashri | 23z228 |
| Lisha | 23z235 |
| Sruthi A | 23z272 |

---

## 📄 License

This project was built as part of an academic mini project assignment.

---

*Built with ❤️ using Groq + LLaMA 3 — NeuralSum*
