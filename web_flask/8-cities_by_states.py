#!/usr/bin/python3
""" module for getting all states in our system
alongside with cities found in that state"""
from flask import Flask, render_template
from models import storage
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(e):
    if storage is not None:
        storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
