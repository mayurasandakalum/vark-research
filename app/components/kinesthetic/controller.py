from flask import render_template


class KinestheticController:
    def show_kinesthetic_page(self):
        print("Kinesthetic page")
        return render_template("kinesthetic/index.html")
