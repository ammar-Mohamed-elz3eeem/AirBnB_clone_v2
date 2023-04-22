#!/usr/bin/python3
"""
states and state modeule: this module will define two routes
into our AirBnB Application:
    1. route for getting all states /states
    2. route for getting single state alongside
        with its cities /state/<string:id>
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(e):
    """teardown db after app is finished"""
    if storage is not None:
        storage.close()


@app.route("/states/<string:uuid>", strict_slashes=False)
def state_route(uuid):
    """Retrieve only single state from states table

    Args:
        uuid (string): id of the state we want to retrive from all states

    Returns:
        string: html page to be rendered on
        reuqest to /states/<string:uuid> route
    """
    states = storage.all("State")
    state = states.get(f"State.{uuid}")
    return render_template("9-states.html", state=state)


@app.route("/states", strict_slashes=False)
def states_route():
    """states_route: will render all states
    saved on database in a 7-states_list.html view template

    Returns:
        string: html page to be rendered on reuqest to /states_list route
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", total=states)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
