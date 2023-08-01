from flask_wtf import FlaskForm
from wtforms import StringField #for the String input
# to put rules on the input; not empty and its length
from wtforms.validators import DataRequired, Length

# class for each form
class Register(Flaskform):
        username = StringField('Username', validators=[DataRequired])
        email=  
        password = 