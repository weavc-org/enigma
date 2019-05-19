import flask

api_bp = flask.Blueprint('api', __name__)

@api_bp.route('/')
def hello_world():
    return 'Hello, World!'