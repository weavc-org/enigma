
#!/usr/bin/env python3 

import flask
from app.view import view_bp

def new_app():

    app = flask.Flask(__name__)
    app.register_blueprint(view_bp)
    app.config['SECRET_KEY'] = 'any secret string'
    return app

