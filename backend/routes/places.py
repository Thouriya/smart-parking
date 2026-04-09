from flask import Blueprint, jsonify
from db import get_db_connection

places_bp = Blueprint('places', __name__)

@places_bp.route('/parking', methods=['GET'])
def get_places():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, zone, status FROM parking_places")
    places = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(places)