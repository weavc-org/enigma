import flask
from web.forms import Form
from enigma.config import config
from enigma.enigma import enigma

view_bp = flask.Blueprint('views', __name__)

@view_bp.route('/', methods=['POST', 'GET'])
def view():

    f = None
    value = ''

    if (flask.request.form):
        f = Form(flask.request.form)
        _config = config()
        en = enigma(_config)
        value = en.encrypt(f.encrypt.data)
    else: 
        f = Form()

    return flask.render_template('view.html', name='chris', form=f, value=value)