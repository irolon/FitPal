import sqlite3
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
from Repository.Usuario_repository import UsuarioRepository

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
        repoUsuarios = UsuarioRepository(sqlite3.connect('data_base/db_fitpal.db'))

        
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400

        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400



        lista_usuarios = repoUsuarios.list()  

        if not lista_usuarios:
            print("No se encontraron usuarios en la base de datos")
            return jsonify({"message": "No users found"}), 404

        for u in lista_usuarios:
            if u.correo == username and u.contrasena == password:
                print("¡LOGIN EXITOSO!")
                return jsonify({
                    "message": "Login successful",
                    "user_id": u.id,
                    "nombre": u.nombre,
                    "apellido": u.apellido,
                    "rol": u.rol
                }), 200

        print("LOGIN FALLIDO: Credenciales no coinciden")
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
# Main
# --------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
