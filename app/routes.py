from flask import render_template
from app import app
from app.components.kinesthetic.controller import KinestheticController


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kinesthetic")
def kinesthetic():
    controller = KinestheticController()
    return controller.show_kinesthetic_page()
