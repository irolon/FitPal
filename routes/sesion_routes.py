from flask import Blueprint, jsonify, request
from Model.Sesion import Sesion
from Service.SesionService import SesionService

def create_sesion_routes(db_connection):
    sesion_routes = Blueprint('sesion_routes', __name__)
    sesion_service = SesionService(db_connection)

    @sesion_routes.route('/sesiones', methods=['GET'])
    def listar_sesiones():
        sesiones = sesion_service.list()
        return jsonify([s.__dict__ for s in sesiones]), 200

    @sesion_routes.route('/sesiones/<int:sesion_id>', methods=['GET'])
    def obtener_sesion(sesion_id):
        sesion = sesion_service.get_by_id(sesion_id)
        if sesion:
            return jsonify(sesion.__dict__), 200
        return jsonify({'error': 'Sesión no encontrada'}), 404

    @sesion_routes.route('/sesiones', methods=['POST'])
    def crear_sesion():
        data = request.get_json()
        sesion = Sesion(
            nombre=data.get('nombre'),
            duracion=data.get('duracion'),
            descripcion=data.get('descripcion')
        )
        nueva_id = sesion_service.add(sesion)
        if nueva_id:
            return jsonify({'id': nueva_id, 'mensaje': 'Sesión creada correctamente'}), 201
        return jsonify({'error': 'Error al crear sesión'}), 400

    @sesion_routes.route('/sesiones/<int:sesion_id>', methods=['PUT'])
    def actualizar_sesion(sesion_id):
        data = request.get_json()
        sesion = Sesion(
            nombre=data.get('nombre'),
            duracion=data.get('duracion'),
            descripcion=data.get('descripcion'),
            id=sesion_id
        )
        resultado = sesion_service.update(sesion)
        if resultado == "Sesión no encontrada":
            return jsonify({'error': resultado}), 404
        return jsonify({'mensaje': resultado}), 200

    @sesion_routes.route('/sesiones/<int:sesion_id>', methods=['DELETE'])
    def eliminar_sesion(sesion_id):
        resultado = sesion_service.delete(sesion_id)
        if resultado == "Sesión no encontrada":
            return jsonify({'error': resultado}), 404
        return jsonify({'mensaje': resultado}), 200

    return sesion_routes
