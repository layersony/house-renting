from flask import render_template, url_for, redirect, request
from . import main
from .. import db, photos
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
  houselisting = House.query.all()
  return render_template('houselisting.html', houselisting=houselisting)

@main.route('/houselist/house/<id>', methods=['GET', 'POST'])
def house(id):
  gethouse = House.query.filter_by(id=id).first()
  reviews = Review.query.filter_by(id=id).all()
  return render_template('viewhouse.html', gethouse=gethouse, reviews=reviews)

@main.route('/review/<id>', methods=['GET', 'POST'])
def review(id):
  house = House.query.filter_by(id=id).first()
  reviehouse = ReviewForm()

  if reviehouse.validate_on_submit():
    reviews = reviehouse.reviewinput.data
    rating = reviehouse.ratinginput.data
    new_review = Review(reviews = reviews, rating=rating)
    new_review.save_review()
    return redirect(url_for('main.house', id=id))
  
  pastreview = Review.query.all()
  return render_template('review.html', reviehouse = reviehouse, pastreview=pastreview, house=house)

@main.route('/search/house/<locationname>', methods=['GET', 'POST'])
def searchhouse(locationname):
  house = House.query.filter_by(location = locationname.capitalize()).all()
  return render_template('searchhouse.html', house=house,locationname = locationname)

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
@login_required
def new_house():
    
    if request.method=='POST':
        house_location=request.form['location']
        house_city=request.form['city']
        house_price=request.form['price']
        house_desc=request.form['desc']
        filename = photos.save(request.files['image'])
        house_image=f'photos/{filename}'
        new_house=house(house_location=house_location,house_city=house_city,house_price=house_price,house_image=house_image,user=current_user, desc=house_desc)

        new_house.save_house()

    return render_template('admin/new_house.html') 

@main.route('/agent/dashboard/<name>', methods=['GET', 'POST'])
@login_required
def agentdash(name):
    houselisting = House.query.all()

    user = User.query.filter_by(username = name).first()
    form = AddPropertyForm()

    if user is None:
      abort(404)
    else:
      print(form.housetype.data)
      if form.validate_on_submit():
        print('inside')
        house = form.housetype.data
        location = form.location.data
        city = form.city.data
        filename = photos.save(request.files['image'])
        house_image=f'photos/{filename}'
        desc = form.description.data
        price = form.price.data
        
        new_house = House(house_type= house, location=location, city=city, images=house_image, desc=desc, price=price)
        new_house.save_house()
        return redirect(url_for('main.agentdash', name=current_user.username))
        
    return render_template('agent/agentdash.html', form=form, houselisting=houselisting)

