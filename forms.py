# Helper file that allows us to ensure that user are giving us the right data ( for example making sure that an email is a valid email )

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit
    email = StringField('Email', validators = [DataRequired(), Email()]) #FlaskForms validator checks if the user entered a valid email and not 
                                                                        #other type of data like a phone number
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()
