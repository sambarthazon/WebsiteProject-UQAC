from calendar import c
from crypt import methods
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from website.models import User
from website import db
from flask_login import login_required, login_user
from werkzeug.security import generate_password_hash


users = Blueprint("users", __name__)


@users.route('/users/list')
@login_required
def index():
    user = User.query.all()
    return render_template('list_users.html', user=user)


@users.route('/user/create', methods=['GET', 'POST'])
@login_required
def create():
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
            flash('User created!')
            return redirect(url_for('users.index')) # Redirection to the home page

    return render_template('create_user.html', user=current_user) # Print the sign-up html page


@users.route('/user/show/<int:user_id>')
@login_required
def show(user_id):
    user = User.query.get(user_id)
    print(user)
    return render_template('show_user.html', user=user)


@users.route('/user/update/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash("User " + user.username + " has been updated", category='success')
        return redirect(url_for('users.index'))
    return render_template('update_user.html', user=user)


@users.route('/user/destroy/<int:user_id>', methods=['GET', 'POST'])
@login_required
def destroy(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash("User " + user.username + " has been deleted!", category='success')
    return redirect(url_for('users.index'))


@users.route('/user/promute/<int:user_id>', methods=['GET', 'POST'])
@login_required
def promute(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.promute = True
        db.session.commit()
        flash("User " + user.username + " has been promuted!", category='success')
    return redirect(url_for('users.index'))