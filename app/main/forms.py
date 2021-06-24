from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, FileField, TextAreaField
from wtforms.validators import Required

class AddPropertyForm(FlaskForm):
  towns = ['Embakasi\r\nKaren\r\nDagoretti\r\nThika\r\nBuruBuru\r\nMakadara\r\n']
  list_of_files = towns[0].split()
  citys = [(x, x) for x in list_of_files]
  
  description = TextAreaField('Home Description', render_kw={'class': 'form-control', 'rows': 15})
  housetype = SelectField('House Type', choices = [('----', '----'), ('Mansion', 'Mansion'), ('Flat', 'Flat'), ('Bedsitter', 'Bedsiter')])
  location = SelectField('Town:', choices=citys)
  city = SelectField('City', choices=[('-----','-----'),('Nairobi','Nairobi')])
  image = FileField('Upload Image')
  price = IntegerField()
  