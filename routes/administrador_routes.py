from flask import Blueprint, request, jsonify
from Service.AdministradorService import AdministradorService
from Model.Administrador import Administrador

administrador_bp = Blueprint('administrador_bp', __name__)
service = AdministradorService("data_base/db_fitpal.db")


@administrador_bp.route('/administradores', methods=['GET'])
def listar_administradores():
    administradores = service.listar()
    return jsonify([dict(a) for a in administradores]) if administradores else jsonify([])


@administrador_bp.route('/administradores/<int:id>', methods=['GET'])
def obtener_administrador(id):
    admin = service.obtener_por_id(id)
    if admin:
        return jsonify(dict(admin))
    return jsonify({"error": "Administrador no encontrado"}), 404


@administrador_bp.route('/administradores', methods=['POST'])
def crear_administrador():
    data = request.json
    nuevo_admin = Administrador(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        contrasena=data["contrasena"],
        activo=data.get("activo", True)
    )
    resultado = service.crear(nuevo_admin)
    return jsonify({"resultado": resultado})


@administrador_bp.route('/administradores/<int:id>', methods=['PUT'])
def actualizar_administrador(id):
    data = request.json
    admin = Administrador(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        contrasena=data["contrasena"],
        activo=data["activo"]
    )
    admin.id = id
    resultado = service.actualizar(admin)
    return jsonify({"resultado": resultado})


@administrador_bp.route('/administradores/<int:id>', methods=['DELETE'])
def eliminar_administrador(id):
    resultado = service.eliminar(id)
    return jsonify({"resultado": resultado})
