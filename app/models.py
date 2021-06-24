from . import db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model): # table for both agent & admin
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(128))
  sname = db.Column(db.String(128))
  username = db.Column(db.String(255))
  email = db.Column(db.String(128))
  phone = db.Column(db.Integer())
  dataJoined = db.Column(db.DateTime, default=datetime.utcnow())
  pass_secure = db.Column(db.String(255))
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

  roles = db.relationship('Role', backref='users', lazy='dynamic')

  @property
  def password(self):
    raise AttributeError("You Can't Read the password attribute")

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)

  def __repr__(self):
    return f'{self.fname} {self.sname}'

class Roles(db.Model): # setting roles for specific users
  __tablename__ = "roles"

  id = db.Column(db.Integer, primary_key=True)
  roleUser = db.Column(db.String(128))

class UserRoles(db.Model): # defining the userrole association table
  __tablename__ = 'user_roles'

  id= db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))

  def admin(self):
    pass
  
  def agent(self):
    pass

class House(db.Model): # house property
  __tablename__ = "house"
  id = db.Column(db.Integer, primary_key=True)
  location = db.Column(db.String(128))
  city = db.Column(db.String(128))
  images = db.Column(db.String())
  house_type = db.Column(db.String(128))
  price = db.Column(db.Integer())
  desc = db.Column(db.String())
  dateposted = db.Column(db.DateTime, default=datetime.utcnow())
  user = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_house(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def delete_house(cls, id):
    todele = cls.query.filter_by(id=id).first()
    db.session.delete(todele)
    db.session.commit()

class Review(db.Model):
  __tablename__ = 'reviews'

  id = db.Column(db.Integer, primary_key=True)
  reviews = db.Column(db.String(255))
  rating = db.Column(db.Integer())

  def save_review(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_spec_reviews(cls, id):
    return cls.query.filter_by(id=id).all()

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))