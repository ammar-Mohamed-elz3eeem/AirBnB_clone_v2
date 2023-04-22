#!/usr/bin/python3
"""
flask web framework module
"""
from flask import Flask, render_template, url_for
from models import storage
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_application():
    amenities = storage.all("Amenity").values()
    states = storage.all("State").values()
    places = storage.all("Place").values()
    print(places)
    return render_template("100-hbnb.html", places=places,
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_db(exit):
    """Close database connection"""
    if storage is not None:
        storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
