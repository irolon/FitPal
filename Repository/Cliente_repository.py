from Model.Usuario import Usuario
from Repository.BaseRepository import BaseRepository
from DAO.Cliente_DAO import ClienteDAO
from DAO.Usuario_DAO import UsuarioDAO

class ClienteRepository(BaseRepository):
    def __init__(self, db_connection):
        super().__init__(db_connection)
        self.cliente_dao = ClienteDAO(db_connection)
        self.usuario_dao = UsuarioDAO(db_connection)
        


    def get_by_id(self, cliente_id):
        try:
            id_cliente = self.cliente_dao.read_by_id(cliente_id)
            if id_cliente is not None:
                return id_cliente
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el cliente por id: {e}")
            return None

    def list(self):
        try:
            clientes = self.cliente_dao.list()
            return clientes
        except Exception as e:
            print(f"Error al listar los clientes: {e}")
            return None

    def add(self, cliente):
        # Verificar si el usuario ya existe
        usuario_existente = self.usuario_dao.read_by_email(cliente.correo)
        
        if usuario_existente:
            return "El usuario ya existe"
        
        try:
            usuario_id = self.usuario_dao.create(cliente)
            
            if usuario_id:
                resultado_cliente = self.cliente_dao.create(usuario_id, cliente)
                return f"Cliente creado exitosamente con ID: {usuario_id}"
            else:
                return "Error al crear el usuario"
                
        except Exception as e:
            print(f"Error al agregar el cliente: {e}")
            return None

    def update(self, cliente):
        try:
            cliente_existente = self.cliente_dao.read_by_id(cliente.id)
            if not cliente_existente:
                return "Cliente no encontrado"
            self.cliente_dao.update(cliente, cliente.id)
            return "Cliente actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el cliente: {e}")
            return None

    def delete(self, cliente_id):
        try:
            cliente_existente = self.cliente_dao.read_by_id(cliente_id)
            if not cliente_existente:
                return "Cliente no encontrado"
            self.cliente_dao.delete(cliente_id)
            return "Cliente eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el cliente: {e}")
            return None