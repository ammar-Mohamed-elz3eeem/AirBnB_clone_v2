#!/usr/bin/python3
"""states and state modeule: this module will define two routes
into our AirBnB Application:
    1. route for getting all states /states
    2. route for getting single state alongside
        with its cities /state/<string:id>
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<string:uuid>", strict_slashes=False)
def state_route(uuid=None):
    """Retrieve only single state from states table, if no uuid passed
    then will return list of all states in database

    Args:
        uuid (string): id of the state we want to retrive from all states

    Returns:
        string: html page to be rendered on
        reuqest to /states/<string:uuid> route
    """
    if uuid is not None:
        state_id = f"State.{uuid}"
    states = storage.all("State")
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(e):
    """teardown db after app is finished"""
    if storage is not None:
        storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
