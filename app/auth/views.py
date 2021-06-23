from flask import render_template,redirect,url_for, flash,request
from app.auth import auth
from ..models import User
from .forms import LoginFormAdmin, RegistrationFormAdmin, ResetFormAdmin,RegistrationFormAgent,LoginFormAgent
from .. import db
from flask_login import login_user

# Admin reg
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationFormAdmin()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = "Admin registration"
    return render_template('auth/admin_register.html',title=title,registration_form = form)

# Admin login 
@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginFormAdmin()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Admin login"
    return render_template('auth/admin_login.html',login_form = login_form,title=title)


# Password reset form
@auth.route('/reset_password',methods=['GET','POST'])
def reset_request():
    reset_form = ResetFormAdmin()
    if reset_form.validate_on_submit():
        user = User.query.filter_by(email = reset_form.email.data).first()
        if user:
            flash('Reset request sent successfully,Check your mail.',"success")
            send_email()
            return redirect(url_for('auth.login'))
    return render_template('reset_request.html',reset_form = reset_form)

# Function specifically for sending reset email
def send_email():
    pass


# -----------------------Agent----------------------------------------------------
