from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/form', methods=['GET', 'POST'])
def form():
    return render_template("form.html", boolean=True)