const btn = document.getElementById('summarizeBtn');
const input = document.getElementById('inputText');
const out = document.getElementById('summary');

btn.addEventListener('click', async () => {
  const text = input.value.trim();
  if (!text) {
    out.textContent = 'Please provide some text to summarize.';
    return;
  }
  out.textContent = 'Summarizing...';
  try {
    const res = await fetch('http://localhost:5000/summarize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      out.textContent = 'Error: ' + (err.error || res.statusText);
      return;
    }
    const data = await res.json();
    out.textContent = data.summary || '(no summary)';
  } catch (e) {
    out.textContent = 'Request failed — is the backend running? ' + e.message;
  }
});
