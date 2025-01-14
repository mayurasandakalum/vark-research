from flask import render_template
from app import app
from app.components.kinesthetic.routes import kinesthetic_bp
from app.components.auditory.routes import auditory_bp
from app.components.visual.routes import visual_bp
from app.components.read_write.routes import read_write_bp


@app.route("/")
def index():
    return render_template("index.html")


# Register the blueprint
app.register_blueprint(kinesthetic_bp, url_prefix="/kinesthetic")
app.register_blueprint(auditory_bp, url_prefix="/auditory")
app.register_blueprint(visual_bp, url_prefix="/visual")
app.register_blueprint(read_write_bp, url_prefix="/readwrite")
