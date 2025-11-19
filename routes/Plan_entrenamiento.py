
from flask import Blueprint, jsonify, request
from Service.Plan_entrenamiento_service import PlanEntrenamientoService
from DAO.Plan_sesion_DAO import PlanSesionDAO
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
        print(f"Datos recibidos para crear plan: {data}")
        
        # Validar campos requeridos
        if not data.get("nombre") or not data.get("cliente_id") or not data.get("administrador_id"):
            return jsonify({"error": "Faltan campos requeridos: nombre, cliente_id, administrador_id"}), 400
        
        # Usar el servicio correctamente
        service = PlanEntrenamientoService('data_base/db_fitpal.db')
        
        nuevo_id = service.add(
            administrador_id=int(data.get("administrador_id")),
            cliente_id=int(data.get("cliente_id")),
            plan_data={
                "nombre": data.get("nombre"),
                "frecuencia": data.get("frecuencia"),
                "fecha_inicio": data.get("fecha_inicio"),
                "fecha_fin": data.get("fecha_fin")
            }
        )

        if nuevo_id:
            return jsonify({"message": "Plan creado exitosamente", "id": nuevo_id}), 201
        else:
            return jsonify({"error": "No se pudo crear el plan"}), 400
            
    except Exception as e:
        print(f"Error admin_create_plan: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


# ======================================================
# ADMIN – editar plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>', methods=['PUT'])
def admin_update_plan(plan_id):
    try:
        data = request.json
        service = PlanEntrenamientoService('data_base/db_fitpal.db')

        actualizado = service.update(plan_id, data)

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


# ======================================================
# ADMIN – obtener sesiones de un plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>/sesiones', methods=['GET'])
def admin_get_plan_sesiones(plan_id):
    try:
        from DAO.Plan_sesion_DAO import PlanSesionDAO
        from data_base.Conexion import Conexion
        
        conn = Conexion('data_base/db_fitpal.db')
        dao = PlanSesionDAO(conn.conexion)
        sesiones = dao.get_sesiones_by_plan_id(plan_id)
        conn.conexion.close()
        
        return jsonify(sesiones), 200
    except Exception as e:
        print(f"Error admin_get_plan_sesiones: {e}")
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – eliminar sesión de un plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>/sesiones/<int:sesion_id>', methods=['DELETE'])
def admin_delete_plan_sesion(plan_id, sesion_id):
    try:
        from DAO.Plan_sesion_DAO import PlanSesionDAO
        from data_base.Conexion import Conexion
        
        conn = Conexion('data_base/db_fitpal.db')
        dao = PlanSesionDAO(conn.conexion)
        eliminado = dao.delete_sesion_from_plan(plan_id, sesion_id)
        conn.conexion.close()
        
        if eliminado:
            return jsonify({"message": "Sesión eliminada del plan"}), 200
        else:
            return jsonify({"error": "No se pudo eliminar la sesión"}), 400
    except Exception as e:
        print(f"Error admin_delete_plan_sesion: {e}")
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – obtener sesiones disponibles para agregar al plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>/sesiones/disponibles', methods=['GET'])
def admin_get_sesiones_disponibles(plan_id):
    try:
        from DAO.Plan_sesion_DAO import PlanSesionDAO
        from data_base.Conexion import Conexion
        
        conn = Conexion('data_base/db_fitpal.db')
        dao = PlanSesionDAO(conn.conexion)
        sesiones = dao.get_sesiones_disponibles(plan_id)
        conn.conexion.close()
        
        return jsonify(sesiones), 200
    except Exception as e:
        print(f"Error admin_get_sesiones_disponibles: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Internal server error"}), 500


# ======================================================
# ADMIN – agregar sesión existente a un plan
# ======================================================
@plan_entrenamiento_bp.route('/admin/planes/<int:plan_id>/sesiones/<int:sesion_id>', methods=['POST'])
def admin_add_sesion_to_plan(plan_id, sesion_id):
    try:
        from DAO.Plan_sesion_DAO import PlanSesionDAO
        from data_base.Conexion import Conexion
        
        conn = Conexion('data_base/db_fitpal.db')
        dao = PlanSesionDAO(conn.conexion)
        agregado = dao.add_sesion_to_plan(plan_id, sesion_id)
        conn.conexion.close()
        
        if agregado:
            return jsonify({"message": "Sesión agregada al plan exitosamente"}), 201
        else:
            return jsonify({"error": "No se pudo agregar la sesión al plan"}), 400
    except Exception as e:
        print(f"Error admin_add_sesion_to_plan: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Internal server error"}), 500
