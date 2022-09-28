from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from website.models import User


class RegistrationForm(FlaskForm):
    service_number = StringField('Service Number', validators=[DataRequired(), Length(min=8, max=8)])
    rank = StringField('Rank', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    sumbit = SubmitField('Create Account')

    @staticmethod
    def validate_username(service_number):
        user = User.query.filter_by(service_number=service_number)
        if user:
            raise ValidationError('That account already exist.')


class LoginForm(FlaskForm):
    service_number = StringField('Service Number', validators=[DataRequired(), Length(min=8, max=8)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    sumbit = SubmitField('Login')
