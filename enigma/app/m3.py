import flask
from app.forms import m3_form
from m3 import settings, enigma

m3_bp = flask.Blueprint('m3', __name__)

@m3_bp.route('/', methods=['GET'])
def redirect():
    return flask.redirect(flask.url_for('m3.view_m3'))

@m3_bp.route('/m3', methods=['POST', 'GET'])
def view_m3():

    f = None
    value = ''

    if flask.request.form:
        f = m3_form(flask.request.form)
        s, err = f.to_data()

        if err != None:
            value = '- ' + '\n- '.join(err)
        else:
            value, err = enigma.enigma(s).encrypt(f.data.data)
    else: 
        f = m3_form()

    return flask.render_template('m3/view.html', form=f, value=value)

@m3_bp.route('/embed/m3', methods=['POST', 'GET'])
def embed_m3():
    f = None
    value = ''

    if flask.request.form:
        f = m3_form(flask.request.form)
        s, err = f.to_data()

        if err != None:
            value = '- ' + '\n- '.join(err)
        else:
            value, err = enigma.enigma(s).encrypt(f.data.data)
    else: 
        f = m3_form()

    return flask.render_template('m3/embed.html', form=f, value=value)

@m3_bp.route('/api/m3', methods=['POST'])
def api_m3():
    content = flask.request.get_json(silent=True)
    if content == None:
        return flask.jsonify(status= 400, errors=["no body supplied"]), 400
        
    data = content.get("input")
    if data == None:
        return flask.jsonify(status=400, errors=["no input provided"]), 400

    s = settings.settings()
    t, err = s.set_values(**content)
    
    if t == False:
        return flask.jsonify(status=400, errors=err), 400

    value, err = enigma.enigma(s).encrypt(data)

    return flask.jsonify(status=200, payload=value, settings=s.to_json())