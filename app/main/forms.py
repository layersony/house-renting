from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, FileField, TextAreaField,  RadioField, widgets
from wtforms.validators import Required

class AddPropertyForm(FlaskForm):
  towns = ['----\r\nKaren\r\nRunda\r\nUmoja\r\nEmbakasi\r\nKasarani\r\nPipeline\r\nThika\r\n']
  list_of_files = towns[0].split()
  citys = [(x, x) for x in list_of_files]
  
  description = TextAreaField('House Description', render_kw={'class': 'form-control', 'rows': 8})
  housetype = SelectField('House Type', choices = [('----', '----'), ('Mansion', 'Mansion'), ('Flat', 'Flat'), ('Bedsitter', 'Bedsiter')])
  location = SelectField('Town:', choices=citys)
  city = SelectField('City', choices=[('-----','-----'),('Nairobi','Nairobi')])
  image = FileField('Upload Image', validators=[Required()])
  price = IntegerField('Price Ksh')
  submit = SubmitField('Submit')

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