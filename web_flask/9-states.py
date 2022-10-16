#!/usr/bin/python3
""" This module starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present ing
    DBStorage sorted by name (A->Z) tip
    """
    state_list = storage.all(State).values()
    return render_template('7-states_list.html', state_list=state_list)


@app.route("/states/<state_id>", strict_slashes=False)
def states_by_id(state_id):
    """ Display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in
    DBStorage sorted by name (A->Z) tip
    """
    state_list = storage.all(State).values()
    for states in state_list:
        if states.id == state_id:
            return render_template('9-states.html',
                                   state=states, state_id=True)
    return render_template('9-states.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
