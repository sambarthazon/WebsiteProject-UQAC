from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)


# Login as a user
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first() # The user to check is the user with this email
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True) # Log in was success
                return redirect(url_for('views.home')) # Redirection to the home page
            else:
                flash("Password is incorrect.", category='error')
        else:
            flash("Email does not exist.", category='error')

    return render_template('login.html', user=current_user) # Print the login html page


# Sign up to the site
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email") # Ask the email
        username = request.form.get("username") # Ask the username
        password1 = request.form.get("password1") # Ask the password
        password2 = request.form.get("password2") # Confirm the password

        email_exists = User.query.filter_by(email=email).first() # Check if the email already exist
        username_exists = User.query.filter_by(username=username).first() # Check if username already exist

        if email_exists:
            flash("Email is already in use.", category='error')
        elif username_exists:
            flash("Username is already in use.", category='error')
        elif password1 != password2:
            flash("Password don\'t match!", category='error')
        elif len(username) < 2:
            flash("Username is too short.", category='error')
        elif len(password1) < 6:
            flash("Password is too short.", category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        elif username == 'Admin1':
            admin = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(admin)
            db.session.commit()
            login_user(admin, remember=True) # Log in as this user when he was registered
            flash('User created!')
            return redirect(url_for('views.home')) # Redirection to the home page
        else: # In case all is ok
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            # New user will have this email, username and password
            db.session.add(new_user) # Add this new user to the database
            db.session.commit() # Refresh the database
            login_user(new_user, remember=True) # Log in as this user when he was registered
            flash('User created!')
            return redirect(url_for('views.home')) # Redirection to the home page

    return render_template('signup.html', user=current_user) # Print the sign-up html page


# Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home')) # Redirection to the home page
