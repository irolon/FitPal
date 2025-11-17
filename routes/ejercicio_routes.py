from flask import Blueprint, request, jsonify
from Service.EjercicioService import EjercicioService

ejercicios_bp = Blueprint("ejercicios", __name__)
service = EjercicioService("data_base/db_fitpal.db")

# ----------------------------
# GET /ejercicios - Listar todos los ejercicios
# ----------------------------
@ejercicios_bp.route("/ejercicios", methods=["GET"])
def obtener_todos():
    try:
        service = EjercicioService("data_base/db_fitpal.db")
        resultado = service.obtener_todos()
        
        if resultado is None or len(resultado) == 0:
            return jsonify([]), 200
        return jsonify(resultado), 200
    
    except Exception as e:
        print(f"Error en obtener_todos: {str(e)}")
        return jsonify({"error": str(e)}), 500

# ----------------------------
# GET /sesion/<id>/ejercicios - Ejercicios de una sesión específica
# ----------------------------
@ejercicios_bp.route("/sesion/<int:sesion_id>/ejercicios", methods=["GET"])
def obtener_ejercicios_sesion(sesion_id):
    try:
        from Service.Sesion_ejercicio_service import SesionEjercicioService
        sesion_ejercicio_service = SesionEjercicioService("data_base/db_fitpal.db")
        
        resultado = sesion_ejercicio_service.obtener_ejercicios_por_sesion(sesion_id)
        
        if resultado is None or len(resultado) == 0:
            return jsonify([]), 200
        return jsonify(resultado), 200
    
    except Exception as e:
        print(f"Error en obtener_ejercicios_sesion: {str(e)}")
        return jsonify({"error": str(e)}), 500

# ----------------------------
# GET /cliente/<id>/ejercicios - Ejercicios de un cliente específico
# ----------------------------
@ejercicios_bp.route("/cliente/<int:cliente_id>/ejercicios", methods=["GET"])
def obtener_ejercicios_cliente(cliente_id):
    try:
        from Service.Sesion_ejercicio_service import SesionEjercicioService
        sesion_ejercicio_service = SesionEjercicioService("data_base/db_fitpal.db")
        
        resultado = sesion_ejercicio_service.obtener_ejercicios_por_cliente(cliente_id)
        
        if resultado is None or len(resultado) == 0:
            return jsonify([]), 200
        return jsonify(resultado), 200
    
    except Exception as e:
        print(f"Error en obtener_ejercicios_cliente: {str(e)}")
        return jsonify({"error": str(e)}), 500




















# # ----------------------------
# # GET /ejercicios/<id>
# # ----------------------------
# @ejercicios_bp.route("/ejercicios/<int:id>", methods=["GET"])
# def obtener_por_id(id):
#     resultado = service.obtener_por_id(id)
#     if "error" in resultado:
#         return jsonify(resultado), 404
#     return jsonify(resultado), 200

# # ----------------------------
# # POST /ejercicios
# # ----------------------------
# @ejercicios_bp.route("/ejercicios", methods=["POST"])
# def crear_ejercicio():
#     data = request.get_json()

#     categoria = data.get("categoria")
#     nombre = data.get("nombre")
#     descripcion = data.get("descripcion", "")
#     repeticiones = data.get("repeticiones", 0)
#     series = data.get("series", 0)
#     descanso = data.get("descanso", 0)

#     resultado = service.crear_ejercicio(categoria, nombre, descripcion, repeticiones, series, descanso)

#     if "error" in resultado:
#         return jsonify(resultado), 400
#     return jsonify(resultado), 201

# # ----------------------------
# # PUT /ejercicios/<id>
# # ----------------------------
# @ejercicios_bp.route("/ejercicios/<int:id>", methods=["PUT"])
# def actualizar_ejercicio(id):
#     data = request.get_json()

#     categoria = data.get("categoria")
#     nombre = data.get("nombre")
#     descripcion = data.get("descripcion", "")
#     repeticiones = data.get("repeticiones", 0)
#     series = data.get("series", 0)
#     descanso = data.get("descanso", 0)

#     resultado = service.actualizar_ejercicio(id, categoria, nombre, descripcion, repeticiones, series, descanso)

#     if "error" in resultado:
#         return jsonify(resultado), 400
#     return jsonify(resultado), 200

# # ----------------------------
# # DELETE /ejercicios/<id>
# # ----------------------------
# @ejercicios_bp.route("/ejercicios/<int:id>", methods=["DELETE"])
# def eliminar_ejercicio(id):
#     resultado = service.eliminar_ejercicio(id)
#     if "error" in resultado:
#         return jsonify(resultado), 404
#     return jsonify(resultado), 200
