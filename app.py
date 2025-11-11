import sqlite3
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS

from DAO.Administrador_DAO import AdministradorDAO
from DAO.Cliente_DAO import ClienteDAO
from DAO.Usuario_DAO import UsuarioDAO
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO
from Repository.Usuario_repository import UsuarioRepository

from Model.Administrador import Administrador
from Model.Cliente import Cliente
from Model.Plan_entrenamiento import PlanEntrenamiento
from Model.Usuario import Usuario

# --------------------------
# Rutas FitPal
# --------------------------
from routes.ejercicios_routes import ejercicios_bp

# --------------------------
# Configuración Flask
# --------------------------
app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:5174",
            "http://127.0.0.1:5174"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# --------------------------
# Login
# --------------------------
@app.route('/api/login', methods=['POST'])
def login():
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400

        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        print(f"Login attempt - Username: {username}, Password: {password}")

        # TODO: Reemplazar por validación real con UsuarioDAO o UsuarioRepository
        if username == "demo" and password == "1234":
            return jsonify({"message": "Login successful", "user_type": "demo"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401

    except Exception as e:
        print(f"Error in login: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# --------------------------
# Registro
# --------------------------
@app.route('/api/register', methods=['POST'])
def register():
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400

        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        name = data.get("name")
        lastname = data.get("lastname")
        dni = data.get("dni")
        edad = data.get("edad")
        email = data.get("email")
        password = data.get("password")

        if not all([name, lastname, dni, edad, email, password]):
            return jsonify({"error": "All fields are required"}), 400

        print(f"Registration attempt - Name: {name}, Lastname: {lastname}, DNI: {dni}, Edad: {edad}, Email: {email}")

        # TODO: Guardar en base de datos usando UsuarioDAO o UsuarioRepository
        return jsonify({"message": "Registration successful"}), 201

    except Exception as e:
        print(f"Error in registration: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# --------------------------
# Registro de Rutas / Blueprints
# --------------------------
app.register_blueprint(ejercicios_bp, url_prefix="/api")

# --------------------------
# Main
# --------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
