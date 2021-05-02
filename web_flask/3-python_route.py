#!/usr/bin/python3
"""Script that starts a flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Prints hello hbnb"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints hello hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Prints hello hbnb"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Python is cool"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
