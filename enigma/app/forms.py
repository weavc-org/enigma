from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from machine.rotors import rotors, reflectors

class Form(FlaskForm):

    rot = []
    for rotor in rotors().all:
        rot.append(rotor.name)

    refl = []
    for reflector in reflectors().all:
        refl.append(reflector.name)
    
    data = StringField('Data: ', [DataRequired(message='Required')])

    left_rotor = SelectField("I", choices=rot)
    middle_rotor = SelectField("II", choices=rot)
    right_rotor = SelectField("III", choices=rot)
    reflector = SelectField("B", choices=refl)

    left_rotor_setting = SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    middle_rotor_setting = SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    right_rotor_setting = SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    left_ring_setting = SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    middle_ring_setting = SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    right_ring_setting = SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))



    submit = SubmitField('Submit')