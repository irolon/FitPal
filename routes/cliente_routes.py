from flask import Blueprint, request, jsonify
from Service.ClienteService import ClienteService
from Model.Cliente import Cliente

cliente_bp = Blueprint('cliente_bp', __name__)
service = ClienteService("data_base/db_fitpal.db")


def _cliente_to_dict(cliente):
    if cliente is None:
        return None
    if hasattr(cliente, "keys") and hasattr(cliente, "__getitem__"):
        return dict(cliente)
    return {
        "usuario_id": getattr(cliente, "id", None) or getattr(cliente, "usuario_id", None),
        "dni": getattr(cliente, "dni", ""),
        "edad": getattr(cliente, "edad", 0),
        "fecha_inicio": getattr(cliente, "fecha_inicio", ""),
    }


@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    
    clientes = service.listar() or []
    clientes_dict = [_cliente_to_dict(c) for c in clientes]
    return jsonify(clientes_dict)


@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def obtener_cliente(id):
    cliente = service.obtener_por_id(id)
    if cliente:
        return jsonify(_cliente_to_dict(cliente))
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


@cliente_bp.route('/admin/clientes', methods=['GET'])
def admin_listar_clientes():
    try:
        # Debug: Usar conexión directa
        import sqlite3
        conn = sqlite3.connect('data_base/db_fitpal.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT u.id, u.nombre, u.apellido, u.correo, c.dni, c.edad
            FROM usuario u 
            LEFT JOIN cliente c ON u.id = c.usuario_id
            WHERE u.rol = 'cliente'
        """)
        
        rows = cursor.fetchall()
        clientes = []
        for row in rows:
            clientes.append({
                'id': row[0],
                'nombre': row[1],
                'apellido': row[2],
                'correo': row[3],
                'dni': row[4] if row[4] else '',
                'edad': row[5] if row[5] else 0,
                'rol': 'cliente'
            })
        
        conn.close()
        return jsonify(clientes), 200
    except Exception as e:
        print(f"Error en admin_listar_clientes: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Error interno del servidor"}), 500
