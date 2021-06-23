from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, RadioField, SelectField, widgets

class RadioField(SelectField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.RadioInput()

class ReviewForm(FlaskForm):
  numb = ['1\r\n2\r\n3\r\n4\r\n5\r\n']
  list_of_files = numb[0].split()
  files = [(x, x) for x in list_of_files]
  reviewinput = TextAreaField('Leave a Review and a Rate')
  ratinginput = RadioField('Rate', choices=files)
  submit = SubmitField('Submit', render_kw={'class': 'btn btn-success'})
  