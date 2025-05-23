from flask import Flask, render_template, request, jsonify
import json
import re
import os

app = Flask(__name__)
LOG_PATH = "logs/traffic.json"

def analyze_log():
    if not os.path.exists(LOG_PATH):
        return []

    alerts = []
    with open(LOG_PATH, "r") as log_file:
        for line in log_file:
            try:
                entry = json.loads(line)
                url = entry.get("url", "")
                body = entry.get("body", "")

                if url.startswith("http://"):
                    alerts.append(f"[!] Insecure protocol used in: {url}")
                if re.search(r"(password|pass|pwd)", body, re.IGNORECASE):
                    alerts.append(f"[!] Password in body: {body[:100]}...")
                if re.search(r"api[_-]?key\s*[:=]\s*['\"]?\w{10,}", body, re.IGNORECASE):
                    alerts.append(f"[!] API key found: {body[:100]}...")
                if re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", body):
                    alerts.append(f"[!] Email found: {body[:100]}...")
                if re.search(r"\b(?:\d[ -]*?){13,16}\b", body):
                    alerts.append(f"[!] Credit card number found: {body[:100]}...")
            except json.JSONDecodeError:
                continue

    return alerts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    alerts = analyze_log()
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)