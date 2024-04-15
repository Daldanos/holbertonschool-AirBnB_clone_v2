#!/usr/bin/python3
"""
0. Hello Flask!
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hnbn():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """display c text"""
    ret_text = text.replace("_", " ")
    return "C {}".format(ret_text)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text):
    """display python text"""
    ret_text = text.replace("_", " ")
    return "Python {}".format(ret_text)


@app.route("/number/<n>", strict_slashes=False)
def num(n):
    """display c text"""
    return "{} is a number".format(n)


@app.route("/number_template/<n>", strict_slashes=False)
def numtem(n):
    """display c text"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
