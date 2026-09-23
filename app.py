from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Version 2 - Automated DevOps Deployment."

@app.route("/status")
def status():
    return "Application Status: ONLINE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)