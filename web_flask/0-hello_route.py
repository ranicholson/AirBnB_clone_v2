#!/usr/bin/python3
"""Script that starts a flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Print greeting"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
