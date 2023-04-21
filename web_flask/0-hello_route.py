#!/usr/bin/env python3
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


if __name__ == "__main__":
    app.run()
