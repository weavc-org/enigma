import flask

view_bp = flask.Blueprint('views', __name__)

@view_bp.route('/')
def view():
    return flask.render_template('view.html', name='chris')

@view_bp.route('/no')
def viewno():
    return flask.render_template('view.html')