from flask import render_template
from app import app
from app.components.kinesthetic.routes import kinesthetic_bp


@app.route("/")
def index():
    return render_template("index.html")


# Register the blueprint
app.register_blueprint(kinesthetic_bp, url_prefix="/kinesthetic")
