from flask import Flask

fapp = Flask(__name__)

@fapp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"