from flask import Blueprint

"""Blueprint of our application. Has a set of urls for each page of this site"""

views = Blueprint('views', __name__)

@views.route('/')
def landing_page():
    return "<hi> TEST</hi>"  # very basic