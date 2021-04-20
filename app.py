from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!, Git push triggered the app!"
