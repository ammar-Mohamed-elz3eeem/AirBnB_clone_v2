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


if __name__ == "__main__":
    app.run('0.0.0.0')
