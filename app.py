import sqlite3
from DAO.Administrador_DAO import AdministradorDAO
from DAO.Cliente_DAO import ClienteDAO
from DAO.Usuario_DAO import UsuarioDAO
from Model.Administrador import Administrador
from Model.Cliente import Cliente
from Model.Plan_entrenamiento import PlanEntrenamiento
from Model.Usuario import Usuario
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO

tabla_usuario = sqlite3.connect('data_base/db_fitpal.db')

# usuario_dao.create_table()

# Ejemplo de uso: agregar un nuevo usuario
# nuevo_usuario = Usuario(nombre="Azul", apellido="Gonzalez", correo="azul.gonzalez@example.com", contrasena="123456", rol="administrador")
# usuario_dao.create(nuevo_usuario)
# print("Usuario agregado con éxito.")

# Ejemplo de uso: mostrar todos los usuarios
# usuarios = usuario_dao.read_all()
# for usuario in usuarios:
#     print(usuario)
    
# Ejemplo de uso: actualizar un usuario
# usuario_existente = Usuario(nombre="Pedro", apellido="Gomez", correo="pedro.gomez@example.com", contrasena="654321", rol="cliente")
# usuario_dao.update(usuario_existente, 2)

# Ejemplo de uso: eliminar un usuario
# usuario_dao.delete(2)
# print("Usuario eliminado con éxito.")

# Mostrar 1 usuario por id
# usuario = usuario_dao.read(1)
# print(usuario)

#cerrar la conexion


# tabla_cliente = sqlite3.connect('data_base/db_fitpal.db')
# cliente_dao = ClienteDAO(tabla_cliente)
# cliente_dao.create_table()

# usuario = usuario_dao.read_by_id(1)
# if not usuario:
#     raise ValueError("Usuario no encontrado")

# nuevo_cliente = Cliente.from_usuario(usuario, dni="12aasss8822", edad=9, fecha_inicio="2027-01-01")
# cliente_dao.create(usuario.id, nuevo_cliente)

# CLIENTE = cliente_dao.read_all()
# print(CLIENTE)

# tabla_admin = sqlite3.connect('data_base/db_fitpal.db')
# administrador_dao = AdministradorDAO(tabla_admin)
# administrador_dao.create_table()
# usuario = usuario_dao.read_by_id(1)
# if not usuario:
#     raise ValueError("Usuario no encontrado")

# nuevo_administrador = Administrador.from_usuario(usuario, activo=True, fecha_alta="2027-01-01")
# administrador_dao.create(usuario.id, nuevo_administrador)
# ADMINISTRADORES = administrador_dao.read_all()
# print(ADMINISTRADORES)

tabla_admin = sqlite3.connect('data_base/db_fitpal.db')
planEntrenamiento_dao = PlanEntrenamientoDAO(tabla_admin)
planEntrenamiento_dao.create_table()
nuevo_plan = PlanEntrenamiento(nombre="fuerza", frecuencia="3 veces por semana", 
                               fecha_inicio="2027-01-01", fecha_fin="2027-03-01")
planEntrenamiento_dao.create(nuevo_plan)