from flask import render_template


class ReadWriteController:
    def show_home_page(self):
        return render_template("read_write_templates/home.html")
