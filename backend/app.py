from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from db import get_connection

app = Flask(__name__)
CORS(app)

# 📁 chemins frontend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, 'frontend', 'html')
CSS_DIR = os.path.join(BASE_DIR, 'frontend', 'css')

# 🟢 page login
@app.route("/")
def home():
    return send_from_directory(HTML_DIR, "login.html")

# 📄 pages HTML
@app.route("/<path:filename>")
def serve_html(filename):
    return send_from_directory(HTML_DIR, filename)

# 🎨 CSS
@app.route("/css/<path:filename>")
def serve_css(filename):
    return send_from_directory(CSS_DIR, filename)



# 🔵 GET PARKING
@app.route("/api/parking", methods=["GET"])
def get_parking():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM parking_places")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

# 🔴 UPDATE STATUS
@app.route("/api/update", methods=["POST"])
def update_status():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE parking_places SET status=%s WHERE id=%s",
        (data["status"], data["id"])
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "updated"})

# 📊 STATS
@app.route("/api/stats", methods=["GET"])
def stats():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT status, COUNT(*) as count
        FROM parking_places
        GROUP BY status
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)