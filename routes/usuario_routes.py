from flask import Blueprint, request, jsonify
from Service.UsuarioService import UsuarioService
from Model.Usuario import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)
service = UsuarioService("data_base/db_fitpal.db")


@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = service.listar()
    return jsonify([dict(u) for u in usuarios]) if usuarios else jsonify([])


@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = service.obtener_por_id(id)
    if usuario:
        return jsonify(dict(usuario))
    return jsonify({"error": "Usuario no encontrado"}), 404


@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        contrasena=data["contrasena"],
        rol=data.get("rol", "cliente")  # valor por defecto
    )
    resultado = service.crear(nuevo_usuario)
    return jsonify({"resultado": resultado})


@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    usuario = Usuario(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        contrasena=data["contrasena"],
        rol=data["rol"],
        id=id
    )
    resultado = service.actualizar(usuario)
    return jsonify({"resultado": resultado})


@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    resultado = service.eliminar(id)
    return jsonify({"resultado": resultado})
