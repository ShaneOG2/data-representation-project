from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import DAO
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

Users = DAO.User()
Users.create_database()
Users.create_user_table()
Notes = DAO.Note()
Notes.create_note_table()

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST": 
        # Get email form form and check user exists
        email = request.form.get("email")
        user_exists = Users.get_user_exists((email))

        if user_exists:
            # Get password from from and real password
            user_inputted_password = request.form.get("password")
            user_password = Users.get_user_password((email))

            #check_password_hash(user_inputted_password, user_password):
            if user_inputted_password == user_password:
                flash('Logged in sucessfully!', category='success')
                user = DAO.OneUser(id = Users.get_user_uid((email)),
                                email = email,
                                password = Users.get_user_password((email)),
                                name = Users.get_user_firstname((email)))
                login_user(user)
                return redirect(url_for("views.home"))
            else:
                flash('Password is inncorrect, please try again.', category='error')
        else:
            flash('Email does not exist, please create an account.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        user_email = request.form.get("email")
        user_firstname = request.form.get("firstName")
        user_password1 = request.form.get("password1")
        user_password2 = request.form.get("password2")

        user_exists = Users.get_user_exists((user_email))
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
            Users.create_user((user_email, 
                            user_password1,
                            #testing - generate_password_hash(user_password1, method='sha256'), 
                            user_firstname))
            flash('Account created!', category='success')
            return redirect(url_for("views.home"))

    return render_template("sign_up.html")