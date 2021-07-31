from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegistrayionForm(FlaskForm):
    username =StringField('Username', validators=[DataRequired(), Length(min=2, max=2)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    password = PasswordField('Password Password', validators=[DataRequired(), EqualTo('password')])