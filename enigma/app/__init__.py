
#!/usr/bin/env python3 

import flask
from app.m3 import m3_bp

def new_app():

    app = flask.Flask(__name__)
    app.register_blueprint(m3_bp)
    app.config['SECRET_KEY'] = 'any secret string'
    return app

