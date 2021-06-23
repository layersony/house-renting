from flask import render_template, url_for, redirect, request
from . import main
from ..models import User, House, Roles, UserRoles, Review
from .forms import ReviewForm

@main.route('/')
def index():
  searchhouse = request.args.get('search')
  if searchhouse:
    redirect(url_for('main.searchhouse', locationname = searchhouse))
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

@main.route('/search/house/<locationname>')
def searchhouse(locationname):
  # house = House.query.filter_by(location = locationname).all()
  house = 'house will display' + locationname
  return render_template('searchhouse.html', house = house)