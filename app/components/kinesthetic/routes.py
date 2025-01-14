from flask import Blueprint
from .controller import KinestheticController

kinesthetic_bp = Blueprint("kinesthetic", __name__)
controller = KinestheticController()


@kinesthetic_bp.route("/")
def index():
    return controller.show_home_page()


# @kinesthetic_bp.route("/home")
# def home():
#     return controller.show_home_page()
