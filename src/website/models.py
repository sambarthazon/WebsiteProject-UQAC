from . import db
from .json_serialize import ma
from flask_login import UserMixin
from sqlalchemy.sql import func


# Users are define by an id, email, username, password, date_created, posts, role, comments and likes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    role = db.Column(db.String(150), default='reader')
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)

    # JSON syntax for users
    def to_json(self):
        return {"id":self.id,
                "username":self.username,
                "email":self.email,
                "role":self.role}


# Posts are define by an id, text, date_created, author, visibility, comments and likes
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    visibility = db.Column(db.String(150), default='public')
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)

    # JSON syntax for posts
    def to_json(self):
        return {"id":self.id,
                "text":self.text,
                "date":self.date_created,
                "author":self.author,
                "visibility":self.visibility}


# Comments are define by an id, text, date_created,author and post_id
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)


# Likes are define by an id, date_created, author and post_id
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)


# Schema for users
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'role')

users_schema = UsersSchema(many=True)


# Schema for posts
class PostsSchema(ma.Schema):
    class Meta:
        fields =('id', 'text', 'date', 'author', 'visibility')

posts_schema = PostsSchema(many=True)