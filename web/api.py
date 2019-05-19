import flask

api_bp = flask.Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/hello')
def hello_world():
    return 'Hello, World!'