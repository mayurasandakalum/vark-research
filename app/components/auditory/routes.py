from flask import Blueprint
from .controller import AuditoryController

auditory_bp = Blueprint("auditory", __name__)
controller = AuditoryController()


@auditory_bp.route("/")
def index():
    return controller.show_home_page()


# @kinesthetic_bp.route("/home")
# def home():
#     return controller.show_home_page()
