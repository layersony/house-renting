from flask import render_template, url_for, redirect, request
from . import main
from ..models import User, House, Roles, UserRoles, Review
from .forms import ReviewForm
from flask import render_template,abort,request,redirect,url_for,flash
from flask_login import login_required,current_user
from .forms import AddPropertyForm

@main.route('/', methods=['GET', 'POST'])
def index():
  lookhouse = request.args.get('search')
  if lookhouse:
    return redirect(url_for('main.searchhouse', locationname = lookhouse))
  else:
    return render_template('index.html')

@main.route('/houselist', methods=['GET', 'POST'])
def houselist():
  p = 'trial'
  return render_template('houselisting.html', p=p)

@main.route('/houselist/house', methods=['GET', 'POST'])
def house():
  # gethouse = House.query.filter_by(id=id).first()
  return render_template('viewhouse.html')

@main.route('/review', methods=['GET', 'POST'])
def review():
  # house = House.query.filter(id=id).first()
  reviehouse = ReviewForm()

  if reviehouse.validate_on_submit():
    reviews = reviehouse.reviewinput.data
    rating = reviehouse.ratinginput.data
    new_review = Review(reviews = reviews, rating=rating)
    new_review.save_review()
    return redirect(url_for('main.houselist'))
  
  pastreview = Review.query.all()
  return render_template('review.html', reviehouse = reviehouse, pastreview=pastreview)

@main.route('/search/house/<locationname>', methods=['GET', 'POST'])
def searchhouse(locationname):
  print(locationname)
  # house = House.query.filter_by(location = locationname).all()
  house = 'house will display' + locationname
  return render_template('searchhouse.html', house = house, locationname = locationname)

@main.route('/about')
def about():
  return render_template('aboutus.html')

@main.route('/admin/index')
def index_admin():
    '''
    View root page function that returns the index page and its data
    '''
    # house=Houses.get_all_houses()
    return render_template('admin/index.html' )


@main.route('/admin/house/new',methods= ['GET','POST'])
# @login_required
def new_house():
    
    if request.method=='POST':
        house_location=request.form['location']
        house_city=request.form['city']
        house_price=request.form['price']
        house_desc=request.form['desc']
        # filename = photos.save(request.files['images'])
        # house_image=f'images/{filename}'
        
        # new_house=house(house_location=house_location,house_city=house_city,house_price=house_price,house_image=house_image,user=current_user)
        new_house=house(house_location=house_location,house_city=house_city,house_price=house_price,house_desc=house_desc,user=current_user)

        new_house.save_house()

    return render_template('admin/new_house.html') 

@main.route('/agent/dashboard', methods=['GET', 'POST'])
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