
from flask import Blueprint, jsonify, request

from Service.Plan_entrenamiento_service import PlanEntrenamientoService
from data_base import Conexion

plan_entrenamiento_bp = Blueprint('plan_entrenamiento_bp', __name__)

@plan_entrenamiento_bp.route('/cliente/<int:cliente_id>/planes', methods=['GET'])
def get_planes_entrenamiento_cliente(cliente_id):
    try:
        service = PlanEntrenamientoService('data_base/db_fitpal.db')
        planes = service.get_by_cliente_id(cliente_id)
        
        if planes is None:
            return jsonify([]), 200
            
        planes_data = [plan.to_dict() for plan in planes]
        return jsonify(planes_data), 200
    except Exception as e:
        print(f"Error fetching training plans: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
