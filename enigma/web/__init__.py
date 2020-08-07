import flask
import waitress

from .m3 import m3_bp

def new_app():

    app = flask.Flask(__name__)
    app.register_blueprint(m3_bp)
    app.config['SECRET_KEY'] = 'any secret string' # need to change this to use env or something
    return app


def start(prod = False):
    app = new_app()
    if prod:
        waitress.serve(app, listen='0.0.0.0:8080')
    else:
        app.run(host='0.0.0.0', port=8080)