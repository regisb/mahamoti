import logging

from flask import Flask, render_template

from . import forms

app = Flask('mahamoti')
app.logger.setLevel(logging.DEBUG)


@app.route("/")
def home():
    return render_template("index.html", forms=forms.instances())
