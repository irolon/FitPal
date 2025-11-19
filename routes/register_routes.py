from flask import Blueprint, request, jsonify
import sqlite3
from Repository.Cliente_repository import ClienteRepository
from Model.Cliente import Cliente
from datetime import datetime


register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    try:

        db_connection = sqlite3.connect('data_base/db_fitpal.db')
        repoClientes = ClienteRepository(db_connection)
        
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

        # Crear el cliente
        nuevo_cliente = Cliente(
            nombre=name, 
            apellido=lastname, 
            correo=email, 
            contrasena=password, 
            dni=dni, 
            edad=edad, 
            fecha_inicio=datetime.now().strftime("%Y-%m-%d")
        )
                
        # Agregar el cliente 
        resultado = repoClientes.add(nuevo_cliente)
        
        if resultado and "exitosamente" in str(resultado):
            return jsonify({"message": "Registro exitoso"}), 201
        elif "ya existe" in str(resultado):
            return jsonify({"error": "Usuario ya existe"}), 409
        else:
            print(f"Error al registrar cliente: {resultado}")
            return jsonify({"error": "Error en el registro"}), 500

    except Exception as e:
        print(f"Error in registration: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500