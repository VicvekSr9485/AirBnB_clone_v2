#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.states import State

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """ This method returns states """
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def shutdown_session(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
