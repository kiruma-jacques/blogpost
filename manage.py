from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Blog, Comments
from flask_migrate import Migrate, MigrateCommand
# import instances
# app=create_app('production')
app=create_app('development')
manager=Manager(app)
migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict (app=app, db=db, User=User, Blog=Blog, Comments=Comments)

if __name__=='__main__':
    manager.run()
