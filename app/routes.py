from flask import Blueprint, request, jsonify
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        user["_id"] = str(user["_id"])
        result.append(user)
    return jsonify(result), 200


@users_bp.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    hashed_password = generate_password_hash(data["password"])
    user_id = mongo.db.users.insert_one(
        {"name": data["name"], "email": data["email"], "password": hashed_password}
    ).inserted_id
    return jsonify({"_id": str(user_id)}), 201


@users_bp.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.json
    mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "User updated successfully"}), 200


@users_bp.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    mongo.db.users.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "User deleted successfully"}), 200
