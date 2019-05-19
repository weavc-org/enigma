import flask
from web.api.api import api_bp

def start():

    app = flask.Flask(__name__)
    app.register_blueprint(api_bp)
    return app