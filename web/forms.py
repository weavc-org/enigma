
from flask_wtf import FlaskForm
from wtforms import (BooleanField, HiddenField, PasswordField, 
    SelectField, StringField, SubmitField, TextAreaField)
from wtforms.validators import (DataRequired, Email, 
    EqualTo, Length, Optional, Regexp, StopValidation, ValidationError)

class Form(FlaskForm):
    encrypt = StringField('Encrypt: ', [DataRequired(message='Required')])
    submit = SubmitField('Submit')