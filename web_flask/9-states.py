#!/usr/bin/python3

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities(id):
    state = storage.get('State', id)
    if state:
        cities = state.cities
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
