from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,length,EqualTo

class LoginForm(FlaskForm):
    account = StringField('account',validators=[DataRequired(),length(min=4,max=10)])
    password = PasswordField('password',validators=[DataRequired()])

    submit = SubmitField('Login')
class RegistrationForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(),length(min=2,max=8)])
    account = StringField('account',validators=[DataRequired(),length(min=4,max=10)])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('userPassword')])

    submit = SubmitField('Sign Up')