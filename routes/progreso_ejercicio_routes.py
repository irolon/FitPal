from flask import Blueprint, request, jsonify
from Service.ProgresoEjercicioService import ProgresoEjercicioService

progreso_ejercicio_bp = Blueprint("progreso_ejercicio", __name__)

# ----------------------------
# GET /progreso-ejercicio/cliente/<id>
# Obtiene el progreso de ejercicios para un cliente
# ----------------------------
@progreso_ejercicio_bp.route("/progreso-ejercicio/cliente/<int:cliente_id>", methods=["GET"])
def obtener_progreso_cliente(cliente_id):
    try:
        service = ProgresoEjercicioService("data_base/db_fitpal.db")
        progreso = service.obtener_progreso_cliente(cliente_id)
                
        return jsonify(progreso), 200
    
    except Exception as e:
        print(f"Error en obtener_progreso_cliente: {str(e)}")
        return jsonify({"error": str(e)}), 500

# ----------------------------
# POST /progreso-ejercicio/actualizar
# Actualiza el estado de un ejercicio para un cliente
# ----------------------------
@progreso_ejercicio_bp.route("/progreso-ejercicio/actualizar", methods=["POST"])
def actualizar_estado_ejercicio():
    try:
        data = request.get_json()
        
        # Validar datos requeridos
        if not data:
            return jsonify({"error": "No se enviaron datos"}), 400
        
        cliente_id = data.get("cliente_id")
        ejercicio_id = data.get("ejercicio_id")
        nuevo_estado = data.get("estado")
        
        if not all([cliente_id, ejercicio_id, nuevo_estado]):
            return jsonify({"error": "Faltan datos requeridos: cliente_id, ejercicio_id, estado"}), 400
        
        service = ProgresoEjercicioService("data_base/db_fitpal.db")
        resultado = service.actualizar_estado_ejercicio(cliente_id, ejercicio_id, nuevo_estado)
        
        
        if "error" in resultado:
            return jsonify(resultado), 400
        
        return jsonify(resultado), 200
    
    except Exception as e:
        print(f"Error en actualizar_estado_ejercicio: {str(e)}")
        return jsonify({"error": str(e)}), 500