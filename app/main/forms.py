from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, FileField, TextAreaField
from wtforms.validators import Required

class AddPropertyForm(FlaskForm):
  towns = ['----\r\nKaren\r\nRunda\r\nUmoja\r\nEmbakasi\r\nKasarani\r\nPipeline\r\nThika\r\n']
  list_of_files = towns[0].split()
  citys = [(x, x) for x in list_of_files]
  
  description = TextAreaField('House Description', render_kw={'class': 'form-control', 'rows': 8})
  housetype = SelectField('House Type', choices = [('----', '----'), ('Mansion', 'Mansion'), ('Flat', 'Flat'), ('Bedsitter', 'Bedsiter')])
  location = SelectField('Town:', choices=citys)
  city = SelectField('City', choices=[('-----','-----'),('Nairobi','Nairobi')])
  image = FileField('Upload Image')
  price = IntegerField('Price Ksh')
  