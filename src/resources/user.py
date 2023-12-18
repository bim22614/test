import uuid
from flask import jsonify, request
from src import app

users = {}

@app.get('/user/<user_id>')
def get_user(user_id):
    if user_id not in users:
        return jsonify(error=f'User with {user_id} id does not exist'), 404
    else:
        user = users[user_id]
        return jsonify(user)


@app.delete('/user/<user_id>')
def delete_user(user_id):
    if user_id not in users:
        return jsonify(error=f'User with {user_id} id does not exist'), 404
    else:
        del users[user_id]
        return f"User deleted by {user_id} id"


@app.post('/user')
def create_user():
    user_name = request.args.get("name")
    user_id = uuid.uuid4().hex
    user = {"id": user_id, "name": user_name}
    users[user_id] = user
    return jsonify(user)


@app.get('/users')
def get_users():
    return list(users.values())
