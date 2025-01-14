from flask import Blueprint
from .controller import VisualController

visual_bp = Blueprint("visual", __name__)
controller = VisualController()


@visual_bp.route("/")
def index():
    return controller.show_home_page()


# @visual_bp.route("/home")
# def home():
#     return controller.show_home_page()
