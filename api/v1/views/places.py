#!/usr/bin/python3
"""view for all Place objects
that handles all default RESTFul API actions"""

from models.city import City
from models.place import Place
from models import storage
from models.user import User

from flask import abort, jsonify, request
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def places_in_city(city_id):
    """Retrieves the list of all Place objects of a city:
    GET /api/v1/cities/<city_id>/places

    If the city_id is not linked to any city object,
                raise a 404 error
        """
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)

    return jsonify([place.to_dict() for place in obj.places])


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves a place object by id

    Args:
        place_id (str): id of the place object to retrieve
    """
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Deletes a place object by id
    Deletes a place object: DELETE /api/v1/places/<place_id>"""
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def add_Place(city_id):
    '''Creates a Place: POST /api/v1/cities/<city_id>/places`'''
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')

        if not data.get('name'):
            abort(400, 'Missing name')

        if not data.get('user_id'):
            abort(400, 'Missing user_id')
    except Exception as e:
        abort(400, 'Not a JSON')

    user = storage.get(User, data.get('user_id'))
    if not user:
        abort(404)
    new_obj = Place(name=data.get('name'), user_id=user.id, city_id=city_id)
    storage.new(new_obj)
    storage.save()

    return jsonify(new_obj.to_dict()), 201


@ app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a place object: PUT /api/v1/places/<place_id>"""
    obj = storage.get(Place, place_id)
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
                or key == 'user_id' or key == 'city_id':
            continue
        setattr(obj, key, value)
        storage.save()

    return jsonify(obj.to_dict()), 200
