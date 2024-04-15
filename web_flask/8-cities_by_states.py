#!/usr/bin/python3
"""
0. Hello Flask!
"""

from flask import Flask, render_template
from models import *
from modes.__init__ import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """display Hello HBNB!"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardowndb(exception):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
