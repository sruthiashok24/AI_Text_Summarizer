# Backend README

Quick notes to run the Flask API used by the frontend.

1. Create and activate a virtual environment (Windows PowerShell example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the API:

```powershell
python app.py
```

The service will listen on `http://0.0.0.0:5000` — verify with `GET /health`.
