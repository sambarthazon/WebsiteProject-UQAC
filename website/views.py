from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post, User, Comment, Like
from . import db


views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    posts = Post.query.all() 
    return render_template("home.html", user=current_user, posts=posts)


# Create a post
@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text: # If the text is empty
            flash('Post cannot be empty', category='error')
        else: # Text available to be upload
            post = Post(text=text, author=current_user.id) # Post will be upload with this text and this author
            db.session.add(post) # Post added to the database
            db.session.commit() # Refresh the database
            flash('Post created!', category='success')
            return redirect(url_for('views.home')) # Redirection to the home page

    return render_template('create_post.html', user=current_user) # Print the create post html page


# Update a post (unfunctional)
@views.route("/update-post/<id>", methods=['GET', 'POST'])
@login_required
def update_post(id):
    posts = Post.query.filter_by(id=id).first() # The post to check is the post with the id in parameters
    if posts.author != current_user: # Only authors can update
        flash("You havn\'t the permission", category='error')
    form = PostForm()
    if form.validate_on_submit():
        posts.text = form.text.data
        db.session.commit() # Refresh the database with the updated post
        flash('Post has been updated', category='success')
        return redirect(url_for('post', post_id=posts.id)) # Redirection to the post page
    elif request.method == 'GET':
        form.text.data = posts.text
    
    return render_template("posts.html", user=current_user, posts=posts) # Print the post html page


# Delete a post
@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first() # The post to check is the post with the id in parameter
    db.session.delete(post) # Post remove from the database
    db.session.commit() # Refresh the database
    flash('Post has been deleted', category='success')
    return redirect(url_for('views.home')) # Redirection to the home page


# User's posts
@views.route("/posts/<username>")
def posts(username):
    user = User.query.filter_by(username=username).first() # The user to check is the user with the username in parameter

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home')) # Redirection to the home page

    posts = user.posts # Take all the user's posts
    return render_template("posts.html", user=current_user, posts=posts, username=username) # Print the posts html page with his posts


# Create a comment in a post
@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text') # We want a text in the comment section

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        post = Post.query.filter_by(id=post_id) # The post to check is the post with the post_id in parameter
        if post:
            comment = Comment(text=text, author=current_user.id, post_id=post_id) # The comment will be with this text, by author, and on this post_id
            db.session.add(comment) # Add the comment to the database
            db.session.commit() # Refresh the database
        else:
            flash('Post does not exist.', category='error')

    return redirect(url_for('views.home')) # Redirection to the home page


# Delete a comment from a post
@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first() # The comment to check is the comment with the comment_id in parameter

    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment) # Delete the comment from the database
        db.session.commit() # Refresh the database

    return redirect(url_for('views.home')) # Redirection to the home page


# Like a post
@views.route("/like-post/<post_id>", methods=['POST'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id).first() # The post to check is the post with the id in parameter
    like = Like.query.filter_by(author=current_user.id, post_id=post_id).first() # The like will be by this author on this post_id

    if not post:
        return jsonify({'error': 'Post does not exist.'}, 400) # Error if the post exist
    elif like:
        db.session.delete(like) # Delete the like from the post
        db.session.commit() # Refresh the database
    else:
        like = Like(author=current_user.id, post_id=post_id) # The like will be by this author on this post_id
        db.session.add(like) # Add the like to the post
        db.session.commit() # Refresh the database

    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)}) # Communication with JavaScript file
