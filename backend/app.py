from flask import Flask, request, jsonify
from summarizer import Summarizer

app = Flask(__name__)
summ = Summarizer()


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json(force=True)
    text = data.get("text", "")
    max_length = data.get("max_length", 130)
    min_length = data.get("min_length", 30)
    if not text:
        return jsonify({"error": "no text provided"}), 400
    summary = summ.summarize(text, max_length=max_length, min_length=min_length)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
