from flask import Blueprint, jsonify, request
from Service.plan_sesion_service import PlanSesionService
from data_base import Conexion as get_db_connection

plan_sesion_bp = Blueprint('plan_sesion_bp', __name__, url_prefix='/api/plan_sesion')

@plan_sesion_bp.route('/', methods=['GET'])
def listar_planes_sesion():
    try:
        service = PlanSesionService(get_db_connection())
        planes = service.obtener_todos()
        return jsonify([p.__dict__ for p in planes]) if planes else jsonify([]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@plan_sesion_bp.route('/<int:id>', methods=['GET'])
def obtener_plan_sesion(id):
    try:
        service = PlanSesionService(get_db_connection())
        plan = service.obtener_por_id(id)
        if plan:
            return jsonify(plan.__dict__), 200
        return jsonify({"error": "Plan de sesión no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@plan_sesion_bp.route('/', methods=['POST'])
def crear_plan_sesion():
    try:
        data = request.get_json()
        service = PlanSesionService(get_db_connection())
        nuevo_plan = service.crear(data)
        return jsonify({"message": "Plan de sesión creado correctamente", "data": nuevo_plan.__dict__}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@plan_sesion_bp.route('/<int:id>', methods=['PUT'])
def actualizar_plan_sesion(id):
    try:
        data = request.get_json()
        data['id'] = id
        service = PlanSesionService(get_db_connection())
        resultado = service.actualizar(data)
        return jsonify({"message": resultado}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@plan_sesion_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_plan_sesion(id):
    try:
        service = PlanSesionService(get_db_connection())
        resultado = service.eliminar(id)
        return jsonify({"message": resultado}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
