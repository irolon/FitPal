from flask import Blueprint, jsonify, request
from Service.plan_sesion_service import PlanSesionService
from Service.SesionService import SesionService
from Service.ProgresoSesionService import ProgresoSesionService
from data_base import Conexion 

plan_sesion_bp = Blueprint('plan_sesion_bp', __name__, url_prefix='/api/plan_sesion')

@plan_sesion_bp.route('/cliente/<int:cliente_id>/sesiones', methods=['GET'])
def obtener_sesiones_cliente(cliente_id):
    try:
        service = ProgresoSesionService('data_base/db_fitpal.db')
        sesiones = service.obtener_sesiones_con_progreso_cliente(cliente_id)

        if sesiones is None or len(sesiones) == 0:
            return jsonify([]), 200
        
        return jsonify(sesiones), 200
    
    except Exception as e:
        print(f"Error en obtener_sesiones_cliente: {str(e)}")
        return jsonify({"error": str(e)}), 500


@plan_sesion_bp.route('/cliente/<int:cliente_id>/sesion/<int:sesion_id>/estado', methods=['PUT'])
def actualizar_progreso_sesion(cliente_id, sesion_id):
    try:
        data = request.get_json()
        estado = data.get('estado', False)  
        service = ProgresoSesionService('data_base/db_fitpal.db') 
        resultado = service.actualizar_progreso_sesion(cliente_id, sesion_id, estado)
        
        if resultado:
            return jsonify({
                "message": "Progreso actualizado correctamente", 
                "estado": estado,
                "cliente_id": cliente_id,
                "sesion_id": sesion_id
            }), 200
        else:
            print("ERROR: El servicio retornó False")
            return jsonify({"error": "No se pudo actualizar el progreso"}), 400
            
    except Exception as e:
        print(f"EXCEPCIÓN en actualizar_progreso_sesion: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# @plan_sesion_bp.route('/', methods=['POST'])
# def crear_plan_sesion():
#     try:
#         data = request.get_json()
#         service = PlanSesionService(get_db_connection())
#         nuevo_plan = service.crear(data)
#         return jsonify({"message": "Plan de sesión creado correctamente", "data": nuevo_plan.__dict__}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @plan_sesion_bp.route('/<int:id>', methods=['PUT'])
# def actualizar_plan_sesion(id):
#     try:
#         data = request.get_json()
#         data['id'] = id
#         service = PlanSesionService(get_db_connection())
#         resultado = service.actualizar(data)
#         return jsonify({"message": resultado}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @plan_sesion_bp.route('/<int:id>', methods=['DELETE'])
# def eliminar_plan_sesion(id):
#     try:
#         service = PlanSesionService(get_db_connection())
#         resultado = service.eliminar(id)
#         return jsonify({"message": resultado}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
