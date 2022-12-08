from flask import Flask
from flask_login import LoginManager
from . import DAO
from flask_sqlalchemy import SQLAlchemy
from os import path


#db = SQLAlchemy()
#DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'PASSWORD'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #from .models import User

    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        user = get_user_by_id()
        return user

    return app
from .auth import users
def get_user_by_id():
    user = DAO.User_Class(uid = "1", email = users.get_user_email_by_uid("1"), password = users.get_user_password_by_uid("1"), name = users.get_user_firstname_by_uid("1"))
    return user