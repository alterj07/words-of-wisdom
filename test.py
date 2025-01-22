from flask import Flask

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return "<p>s19878987</p>"