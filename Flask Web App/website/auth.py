from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import DAO
#from . import db
#from .models import User

auth = Blueprint('auth', __name__)

users = DAO.Users_Class()
users.create_database()
users.create_user_table()

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST": 
        # Get email form form and check user exists
        email = request.form.get("email")
        user_exists = users.get_user_exists((email))
        
        if user_exists:
            #user = User.query.filter_by(email=email).first()
            user = get_user_by_email(email)
            # Get password from from and real password
            user_inputted_password = request.form.get("password")
            user_password = users.get_user_password((email))

            #check_password_hash(user_inputted_password, user_password):
            if user_inputted_password == user_password:
                flash('Logged in sucessfully!', category='success')
                login_user(user, remember = True)
                return redirect(url_for("views.home"))
            else:
                flash('Password is inncorrect, please try again.', category='error')
        else:
            flash('Email does not exist, please create an account.', category='error')

    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        user_email = request.form.get("email")
        user_firstname = request.form.get("firstName")
        user_password1 = request.form.get("password1")
        user_password2 = request.form.get("password2")

        user_exists = users.get_user_exists((user_email))

        if user_exists:
            flash('Email already exists.', category='error')
        elif len(user_email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(user_firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif user_password1 != user_password2:
            flash('Passwords don\'t match.', category='error')
        elif len(user_password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else: 
            users.create_user((user_email, 
                            user_password1,
                            #testing - generate_password_hash(user_password1, method='sha256'), 
                            user_firstname))
            new_user = get_user_by_email(user_email)
            #new_user = User(email=user_email, 
            #                first_name=user_firstname, 
            #                #password=generate_password_hash(user_password1, method='sha256')
            #                password=user_password1
            #                )
            #db.session.add(new_user)
            #db.session.commit()
            login_user(new_user, remember = True)
            flash('Account created!', category='success')
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user = current_user)

def get_user_by_email(email):
    user = DAO.User_Class(uid = users.get_user_uid((email)),
                email = email,
                password = users.get_user_password((email)),
                name = users.get_user_firstname((email)))
    return user