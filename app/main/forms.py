from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField

class ReviewForm(FlaskForm):
  reviewinput = TextAreaField('.')
  submit = SubmitField('Submit')