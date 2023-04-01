from flask import Blueprint, render_template

"""Blueprint of our application. Has a set of urls for each page of this site"""

views = Blueprint('views', __name__,template_folder='templates', static_folder='static')

@views.route('/')
def landing_page():
    return render_template("base.html")

@views.route('/forms')
def form_page():
    return render_template("form.html")