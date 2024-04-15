#!/usr/bin/python3
"""
0. Hello Flask!
"""

from flask import Flask, render_template
from models import *
from modes.__init__ import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display Hello HBNB!"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardowndb(exception):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
