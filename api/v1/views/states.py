#!/usr/bin/python3
"""view for State objects
that handles all default RESTFul API actions"""

from models import storage
from models.state import State

from flask import abort, jsonify, request
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states():
    """
    GET /api/v1/states
    Retrieves the list of all State objects

    Returns:
        list: all State objects
    """

    return jsonify([state.to_dict() for state in storage.all(State).values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object by id

    Args:
        state_id (str): id of the State object to retrieve
    """
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object by id
    Deletes a State object: DELETE /api/v1/states/<state_id>"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@ app_views.route('/states', methods=['POST'], strict_slashes=False)
def add_state():
    '''Creates a State: POST /api/v1/states'''

    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')

        if not data.get('name'):
            abort(400, 'Missing name')
    except Exception as e:
        abort(400, 'Not a JSON')

    new_obj = State(**data)
    storage.new(new_obj)
    storage.save()

    return jsonify(new_obj.to_dict()), 201


@ app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object: PUT /api/v1/states/<state_id>"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key == 'id' or key == 'created_at' or key == 'updated_at':
            continue
        setattr(obj, key, value)
        storage.save()

    return jsonify(obj.to_dict()), 200
