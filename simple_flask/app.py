from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, CI/CD!"

@app.route("/health")
def health():
    return "OK"

@app.route("/sum/<int:a>/<int:b>")
def sum(a, b):
    return str(a + b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)