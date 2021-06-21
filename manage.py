from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Roles, UserRoles, House, Review


app = create_app('development')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
  return dict(app = app, db=db, user=User, Roles=Roles, UserRoles=UserRoles, House=House, Review=Review)

if __name__ == '__main__':
  manager.run()