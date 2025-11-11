from flask import Blueprint, request, jsonify
from Service.ClienteService import ClienteService
from Model.Cliente import Cliente

cliente_bp = Blueprint('cliente_bp', __name__)
service = ClienteService("data_base/escuela.db")


@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = service.listar()
    return jsonify([dict(c) for c in clientes]) if clientes else jsonify([])


@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def obtener_cliente(id):
    cliente = service.obtener_por_id(id)
    if cliente:
        return jsonify(dict(cliente))
    return jsonify({"error": "Cliente no encontrado"}), 404


@cliente_bp.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    nuevo_cliente = Cliente(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        contrasena=data["contrasena"],
        dni=data["dni"],
        edad=data["edad"]
    )
    resultado = service.crear(nuevo_cliente)
    return jsonify({"resultado": resultado})


@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    data = request.json
    cliente = Cliente(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        contrasena=data["contrasena"],
        dni=data["dni"],
        edad=data["edad"],
        id=id
    )
    resultado = service.actualizar(cliente)
    return jsonify({"resultado": resultado})


@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    resultado = service.eliminar(id)
    return jsonify({"resultado": resultado})
