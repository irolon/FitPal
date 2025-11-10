import sqlite3
from DAO.Administrador_DAO import AdministradorDAO
from DAO.Cliente_DAO import ClienteDAO
from DAO.Usuario_DAO import UsuarioDAO
from Model.Administrador import Administrador
from Model.Cliente import Cliente
from Model.Plan_entrenamiento import PlanEntrenamiento
from Model.Usuario import Usuario
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO
from Repository.Usuario_repository import UsuarioRepository

from flask_cors import CORS
from flask import Flask, jsonify, request, send_from_directory


app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:5174", "http://127.0.0.1:5174"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

@app.route('/api/login', methods=['POST'])
def login():
    try:
        # Verificar que se recibió JSON
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        data = request.json
        
        # Verificar que los campos requeridos están presentes
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        username = data.get("username")
        password = data.get("password")
        
        # Validar que los campos no estén vacíos
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        print(f"Login attempt - Username: {username}, Password: {password}")

        # Aquí puedes agregar tu lógica de autenticación real
        if username == "demo" and password == "1234":
            return jsonify({"message": "Login successful", "user_type": "demo"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
            
    except Exception as e:
        print(f"Error in login: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/register', methods=['POST'])
def register():
    try:

        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        data = request.json
        

        if not data:
            return jsonify({"error": "No data provided"}), 401
            
        name = data.get("name")
        lastname = data.get("lastname")
        dni = data.get("dni")
        edad = data.get("edad")
        email = data.get("email")
        password = data.get("password")
        

        if not name or not lastname or not dni or not edad or not email or not password:
            return jsonify({"error": "Name, lastname, dni, edad, email and password are required"}), 400

        print(f"Registration attempt - Name: {name}, Lastname: {lastname}, DNI: {dni}, Edad: {edad}, Email: {email}, Password: {password}")


        return jsonify({"message": "Registration successful"}), 201
            
    except Exception as e:
        print(f"Error in registration: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
