#!/usr/bin/python3
"""
Creates a Flask app; app_views
"""
from flask import jsonify
from api.v1.views import app_views
from models.storage import count


@app_views.route('/status', methods=['GET'])
def api_status():
    """
    Returns a JSON response for RESTFUL API health
    """
    response = {'status': "OK"}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """
    Returns statistics about objects stored in the database
    """
    stats = count()
    return jsonify(stats)
