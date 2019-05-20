
from flask_wtf import FlaskForm
from wtforms import (BooleanField, HiddenField, PasswordField, 
    SelectField, StringField, SubmitField, TextAreaField)
from wtforms.validators import (DataRequired, Email, 
    EqualTo, Length, Optional, Regexp, StopValidation, ValidationError)

class Form(FlaskForm):
    comment = StringField('Make a comment', [DataRequired(message='Comment must not be empty.')])
    other = StringField('Make a other', [DataRequired(message='Other must not be empty.')])
    submit = SubmitField('Submit')