from flask import Flask, redirect, render_template, request, flash
import json

from . import config
from . import forms

app = Flask('mahamoti')
app.secret_key = config.secret_key()


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", forms=forms.instances())

@app.route("/", methods=['POST'])
def validate():
    form = forms.get_class(request.form["name"])(request.form)
    if form.validate():
        log_event(form)
        flash("Activity '{}' logged".format(form.name))
        return redirect("/")
    else:
        return render_template("index.html", forms=forms.instances(form))

def log_event(form):
    event = form.to_dict()
    get_logger().event(json.dumps(event))

def get_logger():
    return config.DebugLogger.instance() if app.debug else config.Logger.instance()
