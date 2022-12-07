from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import DAO
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

Users = DAO.User()
Users.create_database()
Users.create_user_table()
Notes = DAO.Note()
Notes.create_note_table()

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        password = Users.get_user_password("shane.ogorman@coyneresearch.com")
        print("-----------------------------------------")
        print(password)
    if request.method == "POST":
        email = request.form.get("email")
        user_inputed_password = request.form.get("password1")
        user_saved_password = Users.get_user_password(email)
##############################################################################################
        if user:
            if check_password_hash(user.password)
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

        if len(user_email) < 4:
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