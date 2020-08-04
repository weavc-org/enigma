from flask_wtf import FlaskForm
from m3.data import rotors, reflectors
from m3.settings import settings
import wtforms

class m3_form(FlaskForm):

    rot = []
    for rotor in rotors().all:
        rot.append(rotor.name)

    refl = []
    for reflector in reflectors().all:
        refl.append(reflector.name)
    
    data = wtforms.TextAreaField('Data', [wtforms.validators.DataRequired(message='Required')])

    plugboard = wtforms.StringField('Plugboard')

    left_rotor = wtforms.SelectField("I", choices=rot)
    middle_rotor = wtforms.SelectField("II", choices=rot)
    right_rotor = wtforms.SelectField("III", choices=rot)
    reflector = wtforms.SelectField("B", choices=refl)

    left_rotor_setting = wtforms.SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    middle_rotor_setting = wtforms.SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    right_rotor_setting = wtforms.SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    left_ring_setting = wtforms.SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    middle_ring_setting = wtforms.SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    right_ring_setting = wtforms.SelectField("A", choices=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    submit = wtforms.SubmitField('Submit')

    def to_data(self):
        s = settings()
        t, err = s.set_all_values(self.left_rotor.data, self.middle_rotor.data, self.right_rotor.data, \
            self.reflector.data, self.plugboard.data, self.left_ring_setting.data, self.middle_ring_setting.data, \
            self.right_ring_setting.data, self.left_rotor_setting.data, self.middle_rotor_setting.data, \
            self.right_rotor_setting.data)

        if t == False:
            return None, err
        
        return s, None