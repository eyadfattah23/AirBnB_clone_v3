#!usr/bin/python3
'''a module as an index'''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """returns the status of the application
    when /status is visited
    OK if running"""
    return jsonify({'status': 'OK'})
