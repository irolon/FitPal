from flask import Blueprint, request, jsonify
from Service.EjercicioService import EjercicioService
from Service.Sesion_ejercicio_service import SesionEjercicioService

# Constante para la base de datos
DB_PATH = "data_base/db_fitpal.db"

ejercicios_bp = Blueprint("ejercicios", __name__)
service = EjercicioService(DB_PATH)

# ----------------------------
# GET /ejercicios - Listar todos los ejercicios
# ----------------------------
@ejercicios_bp.route("/ejercicios", methods=["GET"])
def obtener_todos():
    try:
        service = EjercicioService(DB_PATH)
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
        sesion_ejercicio_service = SesionEjercicioService(DB_PATH)
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
        sesion_ejercicio_service = SesionEjercicioService(DB_PATH)
        
        resultado = sesion_ejercicio_service.obtener_ejercicios_por_cliente(cliente_id)
        
        if resultado is None or len(resultado) == 0:
            return jsonify([]), 200
        return jsonify(resultado), 200
    
    except Exception as e:
        print(f"Error en obtener_ejercicios_cliente: {str(e)}")
        return jsonify({"error": str(e)}), 500



@ejercicios_bp.route("/admin/ejercicios", methods=["GET"])
def admin_obtener_todos_ejercicios():
    try:
        service = EjercicioService(DB_PATH)
        resultado = service.obtener_todos()

        if resultado is None or len(resultado) == 0:
            return jsonify([]), 200
        return jsonify(resultado), 200

    except Exception as e:
        print(f"Error en admin_obtener_todos_ejercicios: {str(e)}")
        return jsonify({"error": str(e)}), 500






# ============================================================
# ADMIN – Crear Ejercicio  POST /admin/ejercicios
# ============================================================
@ejercicios_bp.route("/admin/ejercicios", methods=["POST"])
def admin_crear_ejercicio():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se enviaron datos"}), 400
            
        service = EjercicioService(DB_PATH)
        
        nuevo_id = service.crear(
            categoria=data.get("categoria"),
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion"),
            repeticiones=data.get("repeticiones"),
            series=data.get("series"),
            descanso=data.get("descanso"),
            estado=data.get("estado", "Activo")
        )

        return jsonify({"mensaje": "Ejercicio creado", "id": nuevo_id}), 201

    except Exception as e:
        print(f"Error admin_crear_ejercicio: {str(e)}")
        return jsonify({"error": str(e)}), 500


# ============================================================
# ADMIN – Actualizar Ejercicio  PUT /admin/ejercicios/<id>
# ============================================================
@ejercicios_bp.route("/admin/ejercicios/<int:ejercicio_id>", methods=["PUT"])
def admin_editar_ejercicio(ejercicio_id):
    try:
        data = request.json
        service = EjercicioService(DB_PATH)

        service.actualizar(
            ejercicio_id,
            categoria=data.get("categoria"),
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion"),
            repeticiones=data.get("repeticiones"),
            series=data.get("series"),
            descanso=data.get("descanso"),
            estado=data.get("estado")
        )

        return jsonify({"mensaje": "Ejercicio actualizado"}), 200

    except Exception as e:
        print(f"Error admin_editar_ejercicio: {str(e)}")
        return jsonify({"error": str(e)}), 500


# ============================================================
# ADMIN – Eliminar Ejercicio  DELETE /admin/ejercicios/<id>
# ============================================================
@ejercicios_bp.route("/admin/ejercicios/<int:ejercicio_id>", methods=["DELETE"])
def admin_eliminar_ejercicio(ejercicio_id):
    try:
        service = EjercicioService(DB_PATH)
        service.eliminar(ejercicio_id)

        return jsonify({"mensaje": "Ejercicio eliminado"}), 200

    except Exception as e:
        print(f"Error admin_eliminar_ejercicio: {str(e)}")
        return jsonify({"error": str(e)}), 500


# ============================================================
# GET /api/admin/ejercicios/<id> - Obtener ejercicio por ID (ADMIN)
# ============================================================
@ejercicios_bp.route("/ejercicios/<int:ejercicio_id>", methods=["GET"])
@ejercicios_bp.route("/admin/ejercicios/<int:ejercicio_id>", methods=["GET"])
def admin_obtener_por_id(ejercicio_id):
    try:
        service = EjercicioService(DB_PATH)
        resultado = service.obtener_por_id(ejercicio_id)

        if not resultado:
            return jsonify({"error": "Ejercicio no encontrado"}), 404

        return jsonify(resultado), 200

    except Exception as e:
        print(f"Error admin_obtener_por_id: {str(e)}")
        return jsonify({"error": str(e)}), 500