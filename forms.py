from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField #for input types
# to put rules on the input; not empty and its length,..etc
from wtforms.validators import DataRequired, Length, Email, EqualTo

# class for each form
class RegisterForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(),Length(min=2, max=20)])
        email = StringField('Email',
                                validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired()])
        confirm_password = PasswordField('Confirm Password',
                                            validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')