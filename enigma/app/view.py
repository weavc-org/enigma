import flask
from app.forms import Form
from machine import settings, enigma

view_bp = flask.Blueprint('views', __name__)

@view_bp.route('/', methods=['POST', 'GET'])
def view():

    f = None
    value = ''

    if (flask.request.form):
        f = Form(flask.request.form)
        s = settings.settings()
        s.set_values(f.left_rotor.data, f.middle_rotor.data, f.right_rotor.data, "C", "xy,sd","a","a","a","a","a","a")
        en = enigma.enigma(s)
        value = en.encrypt(f.data.data)
    else: 
        f = Form()

    return flask.render_template('view.html', name='chris', form=f, value=value)