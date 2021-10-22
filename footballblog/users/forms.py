from flask_wtf.file import FileAllowed
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms import BooleanField
from flask_login import login_required, current_user
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from footballblog.model import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# username and email check if they exist
    def validate_username(self, username):

        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. please choose a different one.')
    def validate_email(self, email):

        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. please choose a different one.')

class Loginform(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    # confirm_password = PasswordField('Confirm Password', validators=[
    #     DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture= FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])] )
    submit = SubmitField('Update')

# username and email check if they exist
    def validate_username(self, username):
        if username.data != current_user.username:

            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. please choose a different one.')
    def validate_email(self, email):
        if email.data != current_user.email:


            user= User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. please choose a different one.')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit =SubmitField('Request Password Reset')
    def validate_email(self, email):

        user= User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])
    submit =SubmitField('Rest Password')
    


