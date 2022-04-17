import json
from flask import Blueprint, jsonify, request
from website.models import User, Post, users_schema, posts_schema
from website import db

# Blueprint for api user
api_user = Blueprint('api_user', __name__, url_prefix="api/user")
# Blueprint for api post
api_post = Blueprint('api_post', __name__, url_prefix="api/post")


# Route for api for users list
@api_user.route("/", methods=['GET'])
def listUsers():
    users = User.query.all()
    res = users_schema.dump(users) #Serialization
    return jsonify({"message":"ok", "data": res}), 200


# Route for api for 1 user
@api_user.route("/<int:id>", methods=['GET'])
def query_user(id):
    user = User.query.get_or_404(id)
    return jsonify({"message":"ok", 'data':user.to_json()}), 200


# Route for api for create user
@api_user.route("/", methods=['PUT'])
def create_user():
    record = json.loads(request.data)
    # requirements to create a user
    user = User(username=record['username'],
                email=record['email'],
                password=record['password'])
    db.session.add(user) # Add user to the database
    db.session.commit()
    return jsonify({"message":"user created", "id":user.id}),201


# Route for api for update user
@api_user.route("/", methods=['POST'])
def update_user():
   record = json.loads(request.data)
   id = record['id']
   user = User.query.get_or_404(id)
   # Parameters of the user we can update
   user.username = record['username']
   user.email = record['email']
   user.role = record['role']
   db.session.commit()
   return jsonify({"message":"user updated", "id":user.id}),204


# Route for api for delete user
@api_user.route("/<int:id>", methods=['DELETE'])
def destroy_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user) # Delete the user from the database
    db.session.commit()
    return jsonify({"message":"user deleted"}),204


# Route for api for posts list
@api_post.route("/", methods=['GET'])
def listPosts():
    posts = Post.query.all()
    res = posts_schema.dump(posts) #Serialization
    return jsonify({"message":"ok", "data": res}), 200


# Route for api for 1 post
@api_post.route("/<int:id>", methods=['GET'])
def query_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({"message":"ok", 'data':post.to_json()}), 200


# Route for api for create a post
@api_post.route("/", methods=['PUT'])
def create_post():
    record = json.loads(request.data)
    # Requirements to create a post
    post = Post(author=record['author'],
                text=record['text'])
    db.session.add(post) # Add the post to the database
    db.session.commit()
    return jsonify({"message":"post created", "id":post.id}),201


# Route for api for update a post
@api_post.route("/", methods=['POST'])
def update_post():
   record = json.loads(request.data)
   id = record['id']
   post = Post.query.get_or_404(id)
   # Parameters we can update
   post.text = record['text']
   db.session.commit()
   return jsonify({"message":"post updated", "id":post.id}),204


# Route for api for delete a post
@api_post.route("/<int:id>", methods=['DELETE'])
def destroy_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post) # Delete the post from the database
    db.session.commit()
    return jsonify({"message":"post deleted"}),204