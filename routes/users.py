from flask import Blueprint, request, jsonify

users_bp = Blueprint('users', __name__)

# Sample data structure for users
users = []

# GET /users - Retrieve a list of all users
@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET /users/<id> - Retrieve a specific user by ID
@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

# POST /users - Create a new user
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT /users/<id> - Update a specific user by ID
@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user['name'] = data.get('name', user['name'])
        user['email'] = data.get('email', user['email'])
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

# DELETE /users/<id> - Delete a specific user by ID
@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 204
