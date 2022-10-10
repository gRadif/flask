from flask import abort, jsonify
from app import app

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

