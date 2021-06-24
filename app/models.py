from . import db, login_manager,create_app
from flask_login import UserMixin, current_user
import app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer #setting time before the token for verification expires


class User(UserMixin, db.Model): # table for both agent & admin
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(128))
  sname = db.Column(db.String(128))
  username = db.Column(db.String(255))
  email = db.Column(db.String(128))
  phone = db.Column(db.Integer())
  dataJoined = db.Column(db.DateTime, default=datetime.utcnow())
  password= db.Column(db.String(255),nullable=False)

  roles = db.relationship('Role', backref='users', lazy='dynamic')

  # handling forgot password
  def get_reset_token(self, expires_sec=1800):
    s = Serializer(create_app("development"),expires_sec)
    return s.dumps({'user_id': self.id}).decode('utf-8')
   
  @staticmethod
  def verify_reset_token(token):
    s = Serializer(create_app("development"))
    try:
      user_id = s.loads(token)['user_id']
    except:
      return None
    return User.query.get(user_id)
    
  def __repr__(self):
    return f"User('{self.username}','{self.email})"
  
  # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

  # @property
  # def password(self):
  #   raise AttributeError("You Can't Read the password attribute")

  # @password.setter
  # def password(self, password):
  #   self.pass_secure = generate_password_hash(password)

  # def verify_password(self, password):
  #   return check_password_hash(self.password, password)



    

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