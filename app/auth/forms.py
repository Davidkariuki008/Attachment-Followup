from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

from ..models.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SignUp')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already taken!!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone NO', validators=[DataRequired()])
    employment_status = SelectField('Employment Status', choices=[('Unemployed', 'Unemployed'),('Employed','Employed')])
    worker_description = TextAreaField('Give a description that best fit you', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    def validate_email(self, field):
        if field.data != current_user.email:
            if User.query.filter_by(email=field.data).first():
                raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if field.data != current_user.username:
            if User.query.filter_by(username = field.data).first():
                raise ValidationError('Username already taken!!')

    def validate_phone(self, field):
        if field.data != current_user.phone_no:
            if User.query.filter_by(phone_no=field.data).first():
                raise ValidationError('Phone number is already in use.')