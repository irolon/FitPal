from flask import Blueprint, jsonify, request
from Service.Sesion_ejercicio_service import SesionEjercicioService
from data_base import Conexion as get_db_connection

sesion_ejercicio_bp = Blueprint('sesion_ejercicio_bp', __name__, url_prefix='/api/sesion_ejercicio')

# Listar ejercicios de una sesión específica
@sesion_ejercicio_bp.route('/<int:sesion_id>', methods=['GET'])
def listar_ejercicios_por_sesion(sesion_id):
    try:
        service = SesionEjercicioService(get_db_connection())
        ejercicios = service.obtener_por_sesion(sesion_id)
        return jsonify([e.__dict__ for e in ejercicios]) if ejercicios else jsonify([]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Agregar ejercicio a sesión
@sesion_ejercicio_bp.route('/<int:sesion_id>', methods=['POST'])
def agregar_ejercicio_a_sesion(sesion_id):
    try:
        data = request.get_json()
        ejercicio_id = data.get('ejercicio_id')
        service = SesionEjercicioService(get_db_connection())
        service.agregar(sesion_id, ejercicio_id)
        return jsonify({"mensaje": "Ejercicio agregado"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Quitar ejercicio de sesión
@sesion_ejercicio_bp.route('/<int:sesion_id>/<int:ejercicio_id>', methods=['DELETE'])
def quitar_ejercicio_de_sesion(sesion_id, ejercicio_id):
    try:
        service = SesionEjercicioService(get_db_connection())
        service.eliminar(sesion_id, ejercicio_id)
        return jsonify({"mensaje": "Ejercicio quitado"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@sesion_ejercicio_bp.route('/<int:id>', methods=['GET'])
def obtener_sesion_ejercicio(id):
    try:
        service = SesionEjercicioService(get_db_connection())
        sesion = service.obtener_por_id(id)
        if sesion:
            return jsonify(sesion.__dict__), 200
        return jsonify({"error": "Sesión de ejercicio no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@sesion_ejercicio_bp.route('/', methods=['POST'])
def crear_sesion_ejercicio():
    try:
        data = request.get_json()
        service = SesionEjercicioService(get_db_connection())
        nueva_sesion = service.crear(data)
        return jsonify({"message": "Sesión de ejercicio creada correctamente", "data": nueva_sesion.__dict__}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@sesion_ejercicio_bp.route('/<int:id>', methods=['PUT'])
def actualizar_sesion_ejercicio(id):
    try:
        data = request.get_json()
        data['id'] = id
        service = SesionEjercicioService(get_db_connection())
        resultado = service.actualizar(data)
        return jsonify({"message": resultado}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@sesion_ejercicio_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_sesion_ejercicio(id):
    try:
        service = SesionEjercicioService(get_db_connection())
        resultado = service.eliminar(id)
        return jsonify({"message": resultado}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
