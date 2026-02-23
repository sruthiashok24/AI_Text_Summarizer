# Project structure and file responsibilities

This document explains the scaffold that was created for the AI Text Summarizer project.

Root layout:

- backend/: Flask API and summarization logic
- frontend/: Minimal static frontend (HTML + JS) that calls the backend
- README.md: original project README


backend/
- `app.py` - Flask application exposing two endpoints:
  - `GET /health` - returns health status
  - `POST /summarize` - accepts JSON `{ "text": "..." }` and returns `{ "summary": "..." }`
- `summarizer.py` - summarization wrapper. It will attempt to load a HuggingFace
  `pipeline('summarization')` using `facebook/bart-large-cnn`. If transformers or
  model loading fails, it falls back to a simple heuristic (first two sentences).
- `requirements.txt` - Python dependencies for the backend.


frontend/
- `index.html` - the UI to paste text and trigger summarization
- `app.js` - front-end logic that sends a `POST` to the backend and renders the response


Data flow / logic
- The frontend collects user text and POSTs to `/summarize`.
- The Flask endpoint passes text to the `Summarizer` wrapper.
- If HF transformers are available and a model can be loaded, the heavy model
  will generate the summary. Otherwise the wrapper returns a short heuristic summary.


Run locally (quick start)

1. Create a Python venv and install backend deps

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
```

2. Start the backend API

```powershell
python backend\app.py
```

3. Open `frontend/index.html` in your browser (double-click the file or use a static file server).

Notes
- Using large Transformers models (BART) requires significant RAM and a suitable
  PyTorch installation. If you don't want to install heavy deps, the wrapper
  will still provide a minimal fallback summary.
