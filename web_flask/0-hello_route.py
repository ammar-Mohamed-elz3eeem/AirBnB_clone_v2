#!/usr/bin/env python3
""" Flask web framework module used for routing /
path with content set to Hello HBNB!
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """ function to handle requests made to / route

    Returns:
        string: content of / route
    """
    return 'Hello HBNB!'


app.run("0.0.0.0")
