

from flask import Blueprint, request, jsonify
import sqlite3
from Repository.Usuario_repository import UsuarioRepository


login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    try:
        db_connection = sqlite3.connect('data_base/db_fitpal.db')
        repoUsuarios = UsuarioRepository(db_connection)

        
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