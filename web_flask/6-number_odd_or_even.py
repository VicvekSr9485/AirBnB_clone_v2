#!/usr/bin/python3
""" This module defines route in flask. """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ This method returns Hello HBNB page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """ This method returns HBNB page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    """ This method returns C page """
    return "C %s" % text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_page(text="is cool"):
    """ This method returns python page """
    if text is not "is cool":
        text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ This method returns number """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ This method returns number template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ This method returns odd or even number """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
