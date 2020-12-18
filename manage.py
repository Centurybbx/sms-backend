from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from global_var import db
from app import db
from app import app
from dao import models
from dao.models import Academy, Class, Course, Major, Student, Teacher


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()