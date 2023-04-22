#!/usr/bin/python3
"""
flask web framework module
"""
from flask import Flask, render_template, url_for
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters_route():
    states = storage.all("State").values()
    amentities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html", states=states, amentities=amentities)


@app.teardown_appcontext
def close_db(exit):
    """Close database connection"""
    if storage is not None:
        storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
