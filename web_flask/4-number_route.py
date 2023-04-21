#!/usr/bin/python3
"""Flask web framework module used for routing /
path with content set to Hello HBNB!"""
from flask import Flask
app = Flask(__name__, )


@app.route('/', strict_slashes=False)
def hello_world():
    """function to handle requests made to / route

    Returns:
        string: content of / route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_func():
    """function to handle requests made to /hbnb route

    Returns:
        string: content of /hbnb route
    """
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_func(text):
    """function to handle requests made to /c/<text> route

    Returns:
        string: c <text>
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False, defaults={"text": "is cool"})
@app.route('/python/<string:text>', strict_slashes=False)
def python_func(text):
    """function to handle requests made to /python/(<text>) route

    Returns:
        string: Python <text = 'is cool'>
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:number>', strict_slashes=False)
def number_func(number):
    """function to handle requests made to /number/<int:number> route

    Returns:
        string: {number} is a number
    """
    return f"{number} is a number"


if __name__ == "__main__":
    app.run('0.0.0.0')
