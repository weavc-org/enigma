import flask
from forms import Form

api_bp = flask.Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/submit', methods=['POST'])
def hello_world():
    f = Form(flask.request.form)
    print (f.comment.data)
    return 'Hello, World!'