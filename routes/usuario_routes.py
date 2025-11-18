from flask import Blueprint, request, jsonify
from Service.UsuarioService import UsuarioService
from Model.Usuario import Usuario


def _usuario_to_dict(usuario):
    """Convierte el modelo Usuario o un sqlite.Row en un diccionario simple."""
    if usuario is None:
        return None

    # sqlite3.Row u objetos similares a mapping
    if hasattr(usuario, "keys") and hasattr(usuario, "__getitem__"):
        return dict(usuario)

    return {
        "id": getattr(usuario, "id", None),
        "nombre": getattr(usuario, "nombre", ""),
        "apellido": getattr(usuario, "apellido", ""),
        "correo": getattr(usuario, "correo", ""),
        "contrasena": getattr(usuario, "contrasena", ""),
        "rol": getattr(usuario, "rol", ""),
    }

usuario_bp = Blueprint('usuario_bp', __name__)
service = UsuarioService("data_base/db_fitpal.db")


@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = service.listar() or []
    usuarios_dict = [_usuario_to_dict(u) for u in usuarios]
    return jsonify(usuarios_dict)


@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = service.obtener_por_id(id)
    if usuario:
        usuario_dict = _usuario_to_dict(usuario)
        return jsonify(usuario_dict)
    return jsonify({"error": "Usuario no encontrado"}), 404


@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        contrasena=data["contrasena"],
        rol=data.get("rol", "cliente")
    )
    resultado = service.crear(nuevo_usuario)
    return jsonify({"resultado": resultado}), 201


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
