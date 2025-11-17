from flask import Blueprint, jsonify, request
from Model.Sesion import Sesion
from Service.SesionService import SesionService

# Constante para la base de datos
DB_PATH = "data_base/db_fitpal.db"

# Blueprint global
sesiones_bp = Blueprint("sesiones", __name__)
service = SesionService(DB_PATH)

# ---- Rutas ----
@sesiones_bp.route('/sesiones', methods=['GET'])
def listar_sesiones():
    sesiones = service.list()
    return jsonify([s.__dict__ for s in sesiones]), 200

@sesiones_bp.route('/sesiones/<int:sesion_id>', methods=['GET'])
def obtener_sesion(sesion_id):
    sesion = service.get_by_id(sesion_id)
    if sesion:
        return jsonify(sesion.__dict__), 200
    return jsonify({'error': 'Sesión no encontrada'}), 404

@sesiones_bp.route('/sesiones', methods=['POST'])
def crear_sesion():
    data = request.get_json()
    sesion = Sesion(
        nombre=data.get('nombre'),
        duracion=data.get('duracion'),
        descripcion=data.get('descripcion')
    )
    nueva_id = service.add(sesion)
    if nueva_id:
        return jsonify({'id': nueva_id, 'mensaje': 'Sesión creada correctamente'}), 201
    return jsonify({'error': 'Error al crear sesión'}), 400

@sesiones_bp.route('/sesiones/<int:sesion_id>', methods=['PUT'])
def actualizar_sesion(sesion_id):
    data = request.get_json()
    sesion = Sesion(
        nombre=data.get('nombre'),
        duracion=data.get('duracion'),
        descripcion=data.get('descripcion'),
        id=sesion_id
    )
    resultado = service.update(sesion)
    if resultado == "Sesión no encontrada":
        return jsonify({'error': resultado}), 404
    return jsonify({'mensaje': resultado}), 200

@sesiones_bp.route('/sesiones/<int:sesion_id>', methods=['DELETE'])
def eliminar_sesion(sesion_id):
    resultado = service.delete(sesion_id)
    if resultado == "Sesión no encontrada":
        return jsonify({'error': resultado}), 404
    return jsonify({'mensaje': resultado}), 200
