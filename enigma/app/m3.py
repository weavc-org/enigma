import flask
from app.forms import m3_form
from m3 import settings, enigma

m3_bp = flask.Blueprint('m3', __name__)

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
        return flask.abort(400)
        
    print(content.get("hello"))
    return flask.jsonify({"hello": "world"})