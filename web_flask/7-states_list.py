#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
"""states_list: this module will have route
/states_list which will get data from storage
and render this states in template 7-states_list.html"""


@app.route("/states_list", strict_slashes=False)
def render_all_states():
    print(storage.all("State"))
    return render_template("7-states_list.html",
                           states=storage.all(State).values())


with app.teardown_appcontext:
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0")
