#!/usr/bin/python3
"""
0. Hello Flask!
"""

from flask import Flask, render_template
from models import *
from modes.__init__ import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """display Hello HBNB!"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardowndb(exception):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
