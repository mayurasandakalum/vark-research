from flask import render_template


class KinestheticController:
    def show_home_page(self):
        return render_template("kinesthetic/home.html")
