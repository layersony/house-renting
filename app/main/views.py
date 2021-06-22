from flask import render_template, url_for, redirect
from . import main
from ..models import User, House, Roles, UserRoles, Review
from .forms import ReviewForm

@main.route('/')
def index():
  heading = 'Working.. Good to go'
  return render_template('index.html', heading=heading)

@main.route('/houselist', methods=['GET', 'POST'])
def houselist():
  p = 'trial'
  return render_template('houselisting.html', p=p)

@main.route('/review/<id>', methods=['GET', 'POST'])
def review(id):
  house = House.query.filter(id=id).first()
  reviehouse = ReviewForm()

  if review.validate_on_submit():
    reviews = ReviewForm.reviewinput.data
    new_review = Review(reviews = reviews)
    new_review.save_review()
    return redirect(url_for('main.houselist'))
  
  pastreview = Review.query.all()
  return render_template('review.html', reviehouse = reviehouse, house=house, pastreview=pastreview)
  