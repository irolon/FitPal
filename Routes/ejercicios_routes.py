from flask import Blueprint, request, jsonify
from services.Ejercicio_service import EjercicioService

ejercicios_bp = Blueprint("ejercicios", __name__)
service = EjercicioService()

# ----------------------------
# GET /ejercicios
# ----------------------------
@ejercicios_bp.route("/ejercicios", methods=["GET"])
def obtener_todos():
    ejercicios = service.obtener_todos()
    return jsonify(ejercicios), 200

# ----------------------------
# GET /ejercicios/<id>
# ----------------------------
@ejercicios_bp.route("/ejercicios/<int:id>", methods=["GET"])
def obtener_por_id(id):
    resultado = service.obtener_por_id(id)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200

# ----------------------------
# POST /ejercicios
# ----------------------------
@ejercicios_bp.route("/ejercicios", methods=["POST"])
def crear_ejercicio():
    data = request.get_json()

    categoria = data.get("categoria")
    nombre = data.get("nombre")
    descripcion = data.get("descripcion", "")
    repeticiones = data.get("repeticiones", 0)
    series = data.get("series", 0)
    descanso = data.get("descanso", 0)

    resultado = service.crear_ejercicio(categoria, nombre, descripcion, repeticiones, series, descanso)

    if "error" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado), 201

# ----------------------------
# PUT /ejercicios/<id>
# ----------------------------
@ejercicios_bp.route("/ejercicios/<int:id>", methods=["PUT"])
def actualizar_ejercicio(id):
    data = request.get_json()

    categoria = data.get("categoria")
    nombre = data.get("nombre")
    descripcion = data.get("descripcion", "")
    repeticiones = data.get("repeticiones", 0)
    series = data.get("series", 0)
    descanso = data.get("descanso", 0)

    resultado = service.actualizar_ejercicio(id, categoria, nombre, descripcion, repeticiones, series, descanso)

    if "error" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado), 200

# ----------------------------
# DELETE /ejercicios/<id>
# ----------------------------
@ejercicios_bp.route("/ejercicios/<int:id>", methods=["DELETE"])
def eliminar_ejercicio(id):
    resultado = service.eliminar_ejercicio(id)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200
