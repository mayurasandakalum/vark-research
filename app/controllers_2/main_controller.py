from flask import render_template


class KinestheticController:
    def show_kinesthetic_page(self):
        return render_template("components/kinesthetic/templates/kinesthetic.html")
