
#!/usr/bin/env python3 

import flask
from web.view import view_bp

def start():

    app = flask.Flask(__name__)
    app.register_blueprint(view_bp)
    app.config['SECRET_KEY'] = 'any secret string'
    return app

