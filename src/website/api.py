import json
from flask import Blueprint, jsonify, request
from website.models import User, Post, users_schema, posts_schema
from website import db

api_user = Blueprint('api_user', __name__, url_prefix="api/user")
api_post = Blueprint('api_post', __name__, url_prefix="api/post")


@api_user.route("/", methods=['GET'])
def listUsers():
    users = User.query.all()
    res = users_schema.dump(users) #Serialization
    return jsonify({"message":"ok", "data": res}), 200


@api_user.route("/<int:id>", methods=['GET'])
def query_user(id):
    user = User.query.get_or_404(id)
    return jsonify({"message":"ok", 'data':user.to_json()}), 200


@api_user.route("/", methods=['PUT'])
def create_user():
    record = json.loads(request.data)
    user = User(username=record['username'],
                email=record['email'],
                password=record['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"user created", "id":user.id}),201


@api_user.route("/", methods=['POST'])
def update_user():
   record = json.loads(request.data)
   id = record['id']
   user = User.query.get_or_404(id)
   user.username = record['username']
   user.email = record['email']
   user.role = record['role']
   db.session.commit()
   return jsonify({"message":"user updated", "id":user.id}),204


@api_user.route("/<int:id>", methods=['DELETE'])
def destroy_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message":"user deleted"}),204



@api_post.route("/", methods=['GET'])
def listPosts():
    posts = Post.query.all()
    res = posts_schema.dump(posts) #Serialization
    return jsonify({"message":"ok", "data": res}), 200


@api_post.route("/<int:id>", methods=['GET'])
def query_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({"message":"ok", 'data':post.to_json()}), 200


@api_post.route("/", methods=['PUT'])
def create_post():
    record = json.loads(request.data)
    post = Post(author=record['author'],
                text=record['text'])
    db.session.add(post)
    db.session.commit()
    return jsonify({"message":"post created", "id":post.id}),201


@api_post.route("/", methods=['POST'])
def update_post():
   record = json.loads(request.data)
   id = record['id']
   post = Post.query.get_or_404(id)
   post.text = record['text']
   db.session.commit()
   return jsonify({"message":"post updated", "id":post.id}),204


@api_post.route("/<int:id>", methods=['DELETE'])
def destroy_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message":"post deleted"}),204