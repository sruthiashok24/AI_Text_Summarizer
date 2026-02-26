from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.1-8b-instant"


def call_llama(prompt: str) -> str:
    """Send a prompt to Groq and return the reply text."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }
    response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=30)
    result = response.json()

    if "choices" not in result:
        raise ValueError(f"Groq error: {result}")

    return result["choices"][0]["message"]["content"]


# ── SERVE FRONTEND ──────────────────────────────────────────────────────────

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")


# ── SUMMARIZE ───────────────────────────────────────────────────────────────

STYLE_PROMPTS = {
    "concise":  "Summarize the following text in a clear, concise paragraph (3-5 sentences):",
    "detailed": "Provide a comprehensive and detailed summary of the following text, covering all key points:",
    "bullet":   "Summarize the following text as a clean bulleted list of key points (use • as bullet character):",
    "eli5":     "Explain the following text as if I were 5 years old, using simple language and analogies:",
    "tweet":    "Summarize the following text in a single tweet (max 280 characters, no hashtags):",
}


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")
    style = data.get("style", "concise")
    language = data.get("language", "English")

    prompt = f"""
Summarize the following text.

Style: {style}
Language: {language}

Text:
{text}
"""

    summary = call_llama(prompt)

    return jsonify({"summary": summary})


# ── ANALYZE ─────────────────────────────────────────────────────────────────

ANALYSIS_PROMPTS = {
    "key-points":   "Extract and list the 5-7 most important key points from the following text. Use numbered list format:",
    "sentiment":    "Analyze the sentiment and tone of the following text. Identify: overall sentiment (positive/negative/neutral/mixed), emotional tone, confidence level, and notable phrases that indicate the sentiment:",
    "entities":     "Extract all named entities from the following text. Organize them into categories: People, Organizations, Locations, Dates/Times, Products/Technologies, and Other. List each entity only once:",
    "questions":    "Generate 5 insightful questions that a reader should ask or consider after reading the following text. Make questions thought-provoking and analytical:",
    "action-items": "Extract all action items, tasks, recommendations, or next steps from the following text. Format as a prioritized checklist:",
}


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "").strip()
    analysis_type = data.get("type", "key-points")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    instruction = ANALYSIS_PROMPTS.get(analysis_type, ANALYSIS_PROMPTS["key-points"])
    prompt = f"{instruction}\n\n{text}"

    try:
        result = call_llama(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── COMPARE ─────────────────────────────────────────────────────────────────

@app.route("/compare", methods=["POST"])
def compare():
    data = request.get_json()
    text_a = data.get("textA", "").strip()
    text_b = data.get("textB", "").strip()

    if not text_a or not text_b:
        return jsonify({"error": "Both texts are required"}), 400

    prompt = f"""Compare and contrast the following two texts. Structure your response as:

1. SIMILARITIES — What themes, ideas, or content do they share?
2. DIFFERENCES — How do they differ in content, tone, or perspective?
3. UNIQUE TO TEXT A — Key points only in the first text
4. UNIQUE TO TEXT B — Key points only in the second text
5. OVERALL ASSESSMENT — Which text is more informative/clear and why?

--- TEXT A ---
{text_a}

--- TEXT B ---
{text_b}"""

    try:
        result = call_llama(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── HEALTH CHECK ─────────────────────────────────────────────────────────────

@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": MODEL})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)