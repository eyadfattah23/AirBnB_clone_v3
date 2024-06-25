#!/usr/bin/python3
"""view for Amenity objects
that handles all default RESTFul API actions"""

from models import storage
from models.amenity import Amenity

from flask import abort, jsonify, request
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities():
    """
    GET /api/v1/amenities
    Retrieves the list of all Amenity objects

    Returns:
        list: all Amenity objects
    """

    return jsonify([amenity.to_dict()
                    for amenity in storage.all(Amenity).values()])


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves a Amenity object by id

    Args:
        amenity_id (str): id of the Amenity object to retrieve
    """
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes a Amenity object by id
    Deletes a Amenity object: DELETE /api/v1/amenities/<amenity_id>"""
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@ app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def add_amenity():
    '''Creates a Amenity: POST /api/v1/amenities'''

    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')

        if not data.get('name'):
            abort(400, 'Missing name')
    except Exception as e:
        abort(400, 'Not a JSON')

    new_obj = Amenity(**data)
    storage.new(new_obj)
    storage.save()

    return jsonify(new_obj.to_dict()), 201


@ app_views.route('/amenities/<amenity_id>',
                  methods=['PUT'], strict_slashes=False)
def update_Amenity(amenity_id):
    """Updates a Amenity object: PUT /api/v1/amenities/<amenity_id>"""
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)

    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
    except Exception as e:
        abort(400, 'Not a JSON')

    for key, value in data.items():
        if key == 'id' or key == 'created_at' or key == 'updated_at':
            continue
        setattr(obj, key, value)
        storage.save()

    return jsonify(obj.to_dict()), 200
