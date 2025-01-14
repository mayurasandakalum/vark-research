from flask import Blueprint
from .controller import ReadWriteController

read_write_bp = Blueprint("readwrite", __name__)
controller = ReadWriteController()


@read_write_bp.route("/")
def index():
    return controller.show_home_page()


# @read_write_bp.route("/home")
# def home():
#     return controller.show_home_page()
