from flask import render_template


class AuditoryController:
    def show_home_page(self):
        return render_template("auditory_templates/home.html")
