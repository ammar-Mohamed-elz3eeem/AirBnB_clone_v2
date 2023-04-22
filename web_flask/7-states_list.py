#!/usr/bin/python3
"""states_list: this module will have route
/states_list which will get data from storage
and render this states in template 7-states_list.html"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(e):
    """teardown db after app is finished"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def render_all_states():
    """render_all_states: will render all states
    saved on database in a 7-states_list.html view template

    Returns:
        string: html page to be rendered om reuqest to /states_list route
    """
    return render_template("7-states_list.html",
                           states=storage.all("State").values())


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
