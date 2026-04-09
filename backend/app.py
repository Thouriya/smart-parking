from flask import Flask, jsonify, request, send_from_directory, session
from flask_cors import CORS
import os
import webbrowser
from threading import Timer
from db import get_connection 

app = Flask(__name__)
CORS(app)

app.secret_key = 'ton_secret_key_ici' # Nécessaire pour les sessions

# 📝 INSCRIPTION
@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", 
                       (data['email'], data['password']))
        conn.commit()
        return jsonify({"message": "Compte créé !"}), 201
    except:
        return jsonify({"error": "Email déjà utilisé"}), 400
    finally:
        cursor.close()
        conn.close()

# 🔑 CONNEXION
@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", 
                   (data['email'], data['password']))
    user = cursor.fetchone()
    
    if user:
        session['user_id'] = user['id']
        return jsonify({"message": "Succès", "role": user['role']}), 200
    return jsonify({"error": "Identifiants incorrects"}), 401

# 📁 Chemins vers le frontend (remonte d'un cran pour sortir de /backend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, '..', 'frontend')
HTML_DIR = os.path.join(FRONTEND_DIR, 'html')
CSS_DIR = os.path.join(FRONTEND_DIR, 'css')

# 🟢 Route d'accueil (Login)
@app.route("/")
def home():
    return send_from_directory(HTML_DIR, "login.html")

# 📄 Servir les pages HTML
@app.route("/<path:filename>")
def serve_html(filename):
    if not filename.endswith(".html"):
        filename += ".html"
    return send_from_directory(HTML_DIR, filename)

# 🎨 Servir le CSS
@app.route("/css/<path:filename>")
def serve_css(filename):
    return send_from_directory(CSS_DIR, filename)

# 🔵 API : Récupérer les places
@app.route("/api/parking", methods=["GET"])
def get_parking():
    conn = get_connection()
    if not conn: return jsonify({"error": "DB connection failed"}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM parking_places")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

# 🔴 API : Mettre à jour une place
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

# --- Lancement automatique ---
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)