
#!/usr/bin/env python3 

import flask
from api import api_bp
from view import view_bp

def start():

    app = flask.Flask(__name__)
    app.register_blueprint(api_bp)
    app.register_blueprint(view_bp)
    app.config['SECRET_KEY'] = 'any secret string'
    return app

app = start()
app.run(host='0.0.0.0', port=5500)
