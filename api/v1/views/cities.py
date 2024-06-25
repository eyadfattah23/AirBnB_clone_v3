#!/usr/bin/python3
"""view for City objects
that handles all default RESTFul API actions"""

from models import storage
from models.state import State
from models.city import City
from flask import abort, jsonify, request
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def cities_in_state(state_id):
    """Retrieves the list of all City objects of a State:
    GET /api/v1/states/<state_id>/cities

    If the state_id is not linked to any State object,
                raise a 404 error
        """
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)

    return jsonify([city.to_dict() for city in obj.cities])


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object by id

    Args:
        city_id (str): id of the City object to retrieve
    """
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object by id
    Deletes a City object: DELETE /api/v1/cities/<city_id>"""
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@ app_views.route('/states/<state_id>/cities',
                  methods=['POST'], strict_slashes=False)
def create_city(state_id):
    '''Creates a State: POST /api/v1/states/<state_id>/cities'''

    state = storage.get(State, state_id)
    if not state:
        abort(404)
    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')

        if not data.get('name'):
            abort(400, 'Missing name')
    except Exception as e:
        abort(400, 'Not a JSON')
    new_obj = City(**data, state_id=state_id)
    storage.new(new_obj)
    storage.save()

    return jsonify(new_obj.to_dict()), 201


@ app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a City object: PUT /api/v1/cities/<city_id>"""
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)

    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
    except Exception as e:
        abort(400, 'Not a JSON')

    for key, value in data.items():
        if key == 'id' or key == 'created_at' or key == 'updated_at'\
                or key == 'state_id':
            continue
        setattr(obj, key, value)
        storage.save()

    return jsonify(obj.to_dict()), 200
