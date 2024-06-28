#!/usr/bin/python3
"""initializes a Flask application"""

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardownApp(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':

    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)  # , debug=1)
