#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    """render template with states
    """
    path = '9-states.html'
    states = storage.all(State)
    return render_template(path, states=states, id=id)


@app.teardown_appcontext
def app_teardown(arg=None):
    """clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
