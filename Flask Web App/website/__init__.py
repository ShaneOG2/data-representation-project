from flask import Flask
from flask_login import LoginManager
from . import DAO
from . import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'PASSWORD'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return get_User(id)

    return app
    
def get_User(x):
    user_id = str(x)
    user_email = auth.users.get_user_email_by_uid(str(x))
    user_password = auth.users.get_user_password_by_uid((str(x)))
    user_name = auth.users.get_user_firstname_by_uid((str(x)))

    user = DAO.User_Class(user_id, user_email, user_password, user_name)

    return user


