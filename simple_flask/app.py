from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    # print datetime with format dd/mm/yyyy hh:mm:ss
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return "Hello, CI/CD! - " + now + "\n"

@app.route("/health")
def health():
    return "OK"

@app.route("/sum/<int:a>/<int:b>")
def sum(a, b):
    if a < 0 or b < 0:
        return "Error: a and b must be non-negative integers"
    return str(a + b)

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    if a < 0 or b < 0:
        return "Error: a and b must be non-negative integers"
    return str(a * b)

# make endpoint for pritn background color in hex
@app.route("/color/<string:color>")
def color(color):
    # check if color is valid hex color
    if len(color) != 6:
        return "Error: color must be a valid hex color"
    try:
        int(color, 16)
    except ValueError:
        return "Error: color must be a valid hex color"
    return "<body style='background-color: #" + color + ";'>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)