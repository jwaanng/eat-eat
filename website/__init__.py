from flask import Flask

def create_app():
    """Function that is used to create Flask application object. Purpose of this function is to initialize the Flask application
    """
    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config['SECRET_KEY'] = 'deeznutsdeeznutsdeeznutsdeeznutsdeeznutsdeeznuts'

    from .views import views

    app.register_blueprint(views, url_prefix='/')  # go to the route
    return app 