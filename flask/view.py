import flask
from forms import Form

view_bp = flask.Blueprint('views', __name__)

@view_bp.route('/')
def view():

    f = Form()
    return flask.render_template('view.html', name='chris', form=f)