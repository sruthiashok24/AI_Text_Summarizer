from typing import Optional

try:
    from transformers import pipeline
except Exception:
    pipeline = None


class Summarizer:
    """Simple summarizer wrapper.

    Attempts to load HuggingFace `pipeline('summarization')` and falls back to
    a lightweight heuristic if transformers aren't available.
    """

    def __init__(self):
        self._pipe = None

    def _load(self):
        if self._pipe is None and pipeline is not None:
            try:
                self._pipe = pipeline("summarization", model="facebook/bart-large-cnn")
            except Exception:
                self._pipe = None

    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> str:
        """Return a summary for `text`.

        If HF transformers are available it will use the model; otherwise it
        returns a short heuristic summary (first two sentences).
        """
        self._load()
        if self._pipe:
            try:
                out = self._pipe(text, max_length=max_length, min_length=min_length)
                return out[0]["summary_text"]
            except Exception:
                pass

        # Fallback: return the first two sentences
        import re

        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        if not sentences:
            return text
        return " ".join(sentences[:2])
