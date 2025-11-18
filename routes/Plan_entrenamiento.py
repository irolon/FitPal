
from flask import Blueprint, jsonify, request
from Service.Plan_entrenamiento_service import PlanEntrenamientoService
from data_base import Conexion

plan_entrenamiento_bp = Blueprint('plan_entrenamiento_bp', __name__)

# ======================================================
# CLIENTE – obtener planes del cliente
# ======================================================
@plan_entrenamiento_bp.route('/cliente/<int:cliente_id>/planes', methods=['GET'])
def get_planes_entrenamiento_cliente(cliente_id):
    try:
        service = PlanEntrenamientoService('data_base/db_fitpal.db')
        planes = service.get_by_cliente_id(cliente_id)
        return jsonify([p.to_dict() for p in planes]) if planes else jsonify([]), 200
    except Exception as e:
        print(f"Error fetching training plans: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – obtener todos los planes
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes', methods=['GET'])
def admin_get_planes():
    try:
        service = PlanEntrenamientoService('data_base/db_fitpal.db')
        planes = service.get_all()
        return jsonify([p.to_dict() for p in planes]), 200
    except Exception as e:
        print(f"Error admin_get_planes: {e}")
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – obtener plan por ID
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>', methods=['GET'])
def admin_get_plan(plan_id):
    try:
        service = PlanEntrenamientoService('data_base/db_fitpal.db')
        plan = service.get_by_id(plan_id)
        if not plan:
            return jsonify({"error": "Plan no encontrado"}), 404
        return jsonify(plan.to_dict()), 200
    except Exception as e:
        print(f"Error admin_get_plan: {e}")
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – crear plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes', methods=['POST'])
def admin_create_plan():
    try:
        data = request.json
        service = PlanEntrenamientoService('data_base/db_fitpal.db')

        nuevo_id = service.create(
            nombre=data.get("nombre"),
            administrador_id=data.get("administrador_id"),
            cliente_id=data.get("cliente_id"),
            frecuencia=data.get("frecuencia"),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin")
        )

        return jsonify({"message": "Plan creado", "id": nuevo_id}), 201
    except Exception as e:
        print(f"Error admin_create_plan: {e}")
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – editar plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>', methods=['PUT'])
def admin_update_plan(plan_id):
    try:
        data = request.json
        service = PlanEntrenamientoService('data_base/db_fitpal.db')

        actualizado = service.update(
            plan_id,
            nombre=data.get("nombre"),
            frecuencia=data.get("frecuencia"),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            cliente_id=data.get("cliente_id")
        )

        if not actualizado:
            return jsonify({"error": "Plan no encontrado"}), 404

        return jsonify({"message": "Plan actualizado"}), 200
    except Exception as e:
        print(f"Error admin_update_plan: {e}")
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – eliminar plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>', methods=['DELETE'])
def admin_delete_plan(plan_id):
    try:
        service = PlanEntrenamientoService('data_base/db_fitpal.db')
        eliminado = service.delete(plan_id)

        if not eliminado:
            return jsonify({"error": "Plan no encontrado"}), 404

        return jsonify({"message": "Plan eliminado"}), 200
    except Exception as e:
        print(f"Error admin_delete_plan: {e}")
        return jsonify({"error": "Internal server error"}), 500
