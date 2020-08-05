
#!/usr/bin/env python3 

import flask
from web.m3 import m3_bp

def new_app():

    app = flask.Flask(__name__)
    app.register_blueprint(m3_bp)
    app.config['SECRET_KEY'] = 'any secret string'
    return app

def start():
    server = new_app()
    server.run(host='0.0.0.0', port=5501)