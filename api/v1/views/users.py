#!/usr/bin/python3
"""view for User objects
that handles all default RESTFul API actions"""
from models import storage
from models.user import User

from flask import abort, jsonify, request
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """
    GET /api/v1/users
    Retrieves the list of all User objects

    Returns:
        list: all User objects
    """

    return jsonify([user.to_dict() for user in storage.all(User).values()])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_User(user_id):
    """Retrieves a User object by id

    Args:
        user_id (str): id of the User object to retrieve
    """
    obj = storage.get(User, user_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_User(user_id):
    """Deletes a User object by id
    Deletes a User object: DELETE /api/v1/users/<user_id>"""
    obj = storage.get(User, user_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@ app_views.route('/users', methods=['POST'], strict_slashes=False)
def add_User():
    '''Creates a User: POST /api/v1/users'''

    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')

        if not data.get('name'):
            abort(400, 'Missing name')

        if not data.get('email'):
            abort(400, 'Missing email')

        if not data.get('password'):
            abort(400, 'Missing password')
    except Exception as e:
        abort(400, 'Not a JSON')

    new_obj = User(**data)
    storage.new(new_obj)
    storage.save()

    return jsonify(new_obj.to_dict()), 201


@ app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_User(user_id):
    """Updates a User object: PUT /api/v1/users/<user_id>"""
    obj = storage.get(User, user_id)
    if not obj:
        abort(404)

    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
    except Exception as e:
        abort(400, 'Not a JSON')

    for key, value in data.items():
        if key == 'id' or key == 'created_at' or key == 'updated_at' \
                or key == 'email':
            continue
        setattr(obj, key, value)
        storage.save()

    return jsonify(obj.to_dict()), 200
