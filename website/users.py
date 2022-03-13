from calendar import c
from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models import User
from website import db
from flask_login import login_required


users = Blueprint("users", __name__)


@users.route("/list-user")
@login_required
def index():
    user = User.query.all()
    return render_template('list_users.html', user=user)


@users.route("/show-user")
@login_required
def show(user_id):
    user = User.query.get(user_id)
    print(user)
    return render_template("show_user.html", user=user)


@users.route("/update-user")
def update(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash("User" + user.username + "has been updated", category="success")
        return redirect(url_for('users.list-user'))
    return render_template("update_user.html")


@users.route("/destroy-user")
@login_required
def destroy(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User has been deleted!", category="success")
    return redirect(url_for('users.show-user'))