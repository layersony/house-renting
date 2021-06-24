from flask import render_template,redirect,url_for, flash,request
from app.auth import auth
from ..models import User
from .forms import LoginFormAdmin, LoginFormAgent, RegistrationFormAdmin,RegistrationFormAgent,ContactUsForm
from .. import db,bcrypt,create_app,mail
from flask_login import login_required,login_user,current_user,logout_user
from flask_mail import Message
# Admin reg
@auth.route('/register',methods = ["POST","GET"])
def register():
    form = RegistrationFormAdmin()
    
    if form.validate_on_submit():
        
        user = User(username=form.username.data, email = form.email.data, password=form.password.data)
        
        db.session.add(user)
        
        db.session.commit()
        
        return  redirect(url_for('auth.login'))
        
    title = "Admin login"
    
    return render_template('auth/admin_register.html',form=form,title=title )

# Admin login 
@auth.route('/login',methods = ['POST','GET'])
def login():
    
    form = LoginFormAdmin()
    
    if form.validate_on_submit():
        
        user = User.query.filter_by(email = form.email.data).first()
        
        if user is not None and user.verify_password(form.password.data):
            
            login_user(user,form.remember.data)
            
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid username or Password')
    
    title = "Admin login"
    
    return render_template('auth/admin_login.html',form = form,title=title)


# logout
@auth.route('/logout')

@login_required

def logout():
    
    logout_user()
    
    return redirect(url_for("main.index"))

@auth.route('/contact',methods = ['POST','GET'])
def customer_feedback():

    form = ContactUsForm()
    
    if form.validate_on_submit():
        
        user = User(username=form.full_name.data, email = form.email.data)        
        
        db.session.add(user)
        
        db.session.commit()
            
    title = "Contact us"
    
    return render_template('auth/contact.html',form = form,title=title)
# # Agent Registration
# # Admin reg
# @auth.route('/agent',methods = ["GET","POST"])
# def register():
    
#     form = RegistrationFormAgent()
    
#     if form.validate_on_submit():
        
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
       
#         user = User(email = form.email.data, username = form.username.data, password = hashed_password)

        
#         db.session.add(user)
        
#         db.session.commit()
        
#         flash("Account successfully created. Proceed with Login")
        
#         return redirect(url_for('auth.login'))
    
#     title = "Admin registration"
    
#     return render_template('auth/agent_register.html',title=title,form = form)



# # # Function specifically for sending reset email
# def send_reset_email(user):
#     token = user.get_reset_token()
#     msg = Message('Password Reset Request',
#                   sender='noreply@demo.com',
#                   recipients=[user.email])
#     msg.body = f'''To reset your password, visit the following link:
# {url_for('reset_token', token=token, _external=True)}
# If you did not make this request then simply ignore this email and no changes will be made.
# '''
#     mail.send(msg)

# # Password reset form
# @auth.route("/reset_password", methods=['GET', 'POST'])
# def reset_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index'))
#     form = RequestResetForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         send_reset_email(user)
#         flash('An email has been sent with instructions to reset your password.', 'info')
#         return redirect(url_for('login'))
#     return render_template('reset_request.html', title='Reset Password', form=form)


# @auth.route("/reset_password/<token>", methods=['GET', 'POST'])
# def reset_token(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     user = User.verify_reset_token(token)
#     if user is None:
#         flash('That is an invalid or expired token', 'warning')
#         return redirect(url_for('reset_request'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user.password = hashed_password
#         db.session.commit()
#         flash('Your password has been updated! You are now able to log in', 'success')
#         return redirect(url_for('login'))
#     return render_template('reset_token.html', title='Reset Password', form=form)

# # -----------------------Agent----------------------------------------------------
# Agent reg
@auth.route('/register_agent',methods = ["POST","GET"])
def register_agent():
    form = RegistrationFormAgent()
    
    if form.validate_on_submit():
        
        user = User(username=form.username.data, email = form.email.data, password=form.password.data)
        
        db.session.add(user)
        
        db.session.commit()
        
        return  redirect(url_for('auth.login_agent'))
        
    title = "Agent login"
    
    return render_template('auth/agent_register.html',form=form,title=title )

# Agent login 
@auth.route('/login_agent',methods = ['POST','GET'])
def login_agent():
    
    form = LoginFormAgent()
    
    if form.validate_on_submit():
        
        user = User.query.filter_by(email = form.email.data).first()
        
        if user is not None and user.verify_password(form.password.data):
            
            login_user(user,form.remember.data)
            
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid username or Password')
    
    title = "Admin login"
    
    return render_template('auth/agent_login.html',form = form,title=title)


# logout
