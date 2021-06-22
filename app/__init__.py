from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES



db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
photos = UploadSet('photos', IMAGES)


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
  app = Flask(__name__)

  app.config.from_object(config_options[config_name])

  login_manager.init_app(app)
  db.init_app(app)
  bootstrap.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  
  app.register_blueprint(auth_blueprint, url_prefix= '/authenticate')

  from .request import configure_request
  configure_request(app)
  
  configure_uploads(app,photos)

  return app
  