from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from wtforms import ValidationError
from app.models import User
# Registration form
class RegistrationFormAdmin(FlaskForm):
    """
    class for registration of Admin
    """
    full_name = StringField("Full name",validators=[DataRequired(),Length(min = 3,max =30)])
    username = StringField("Username",validators=[DataRequired(),Length(min = 3,max =20)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    phone = StringField("Phone",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),])
    confirm_password = PasswordField("Password Confirm",validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Register")

        # custom validators
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

# Admin login form
class LoginFormAdmin(FlaskForm):
    """
    class for login of Admin
    """
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),])
    remember = BooleanField("Remember me")
    submit = SubmitField("Submit")

# Agent Registration form
class RegistrationFormAgent(FlaskForm):
    """
    class for registration of Agent
    """
    full_name = StringField("Full name",validators=[DataRequired(),Length(min = 3,max =30)])
    username = StringField("Username",validators=[DataRequired(),Length(min = 3,max =20)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    phone = StringField("Phone",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),])
    confirm_password = PasswordField("Password Confirm",validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Register")

    # custom validators
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

# Agent login form
class LoginFormAgent(FlaskForm):
    """
    class for login of Agent
    """
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),])
    remember = BooleanField("Remember me")
    submit = SubmitField("Submit")