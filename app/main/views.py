from flask import render_template, abort
from . import main
from ..models import User, House
from .forms import AddPropertyForm

# @main.route('/')
# def index():
#   heading = 'Working.. Good to go'
#   return render_template('index.html', heading=heading)

@main.route('/', methods=['GET', 'POST'])
def agentdash():
  user = User.query.filter_by(name = name).first()

  if user is None:
    abort(404)
  else:
    form = AddPropertyForm()

    if form.validate_on_submit():
      house = form.housetype.data
      location = form.location.data
      city = form.city.data
      image = form.image.data
      desc = form.description.data
      price = form.price.data
      
      new_house = House(house, location, city, image, desc, price)
      new_house.save_house()
      return redirect(url_for('main.agentdash'))
      
    return render_template('agent/agentdash.html', form=form)

