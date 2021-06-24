from flask import render_template
from . import main
from flask import render_template,abort,request,redirect,url_for,flash
from flask_login import login_required,current_user
from ..models import User,House
from .. import db




@main.route('/home')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html' )

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
        filename = photos.save(request.files['images'])
        house_image=f'images/{filename}'
        
        new_house=house(house_location=house_location,house_city=house_city,house_price=house_price,house_image=house_image,user=current_user)
        new_house.save_house()

    return render_template('admin/new_house.html') 

