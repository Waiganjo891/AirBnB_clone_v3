#!/usr/bin/python3
"""
Create states
"""
from flask import jsonify, abort
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/states', strict_slashes=False)
def get_all_states():
    """
    Retrieves a list of all states objects
    """
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    """
    """
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        return abort(404)


@app_views.route('/states/<state_id>', method=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """
    """
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states', method=['POST'], strict_slashes=False)
def create_state():
    """
    """
    if request.content_type != 'application/json':
        return abort(404, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')
