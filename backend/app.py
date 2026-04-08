from flask import Flask, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

# 🔵 GET all parking places
@app.route("/api/parking", methods=["GET"])
def get_parking():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM parking_places")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

# 🔴 UPDATE status (simulation capteurs)
@app.route("/api/update/<int:id>/<status>", methods=["GET"])
def update_status(id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE parking_places SET status=%s WHERE id=%s",
        (status, id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "updated", "id": id, "status": status})

if __name__ == "__main__":
    app.run(debug=True)