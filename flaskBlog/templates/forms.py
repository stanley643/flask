from email.policy import EmailPolicy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    username = StringField('username', 
                            validators =[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                         validators =[DataRequired(), EmailPolicy()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
        email = StringField('Email',
                            validators =[DataRequired(), Email()])
        password = PasswordField('password', validators=[DataRequired()])
        remember = BooleanField('Remember Me')
        submit = SubmitField('login')