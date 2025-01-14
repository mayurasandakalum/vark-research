from flask import render_template


class VisualController:
    def show_home_page(self):
        return render_template("visual_templates/home.html")
