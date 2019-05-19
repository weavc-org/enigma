
import flask
from web.api import api_bp
from web.view import view_bp

def start():

    app = flask.Flask(__name__)
    app.register_blueprint(api_bp)
    app.register_blueprint(view_bp)
    return app