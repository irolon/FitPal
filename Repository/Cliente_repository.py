from Repository.BaseRepository import BaseRepository
from DAO.Cliente_DAO import ClienteDAO

class ClienteRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.base_repository = BaseRepository(db_connection)
        self.cliente_dao = ClienteDAO(db_connection)
        
    def get_by_id(self, usuario_id):
        try:
            id_cliente = self.cliente_dao.read_by_id(usuario_id)
            if(id_cliente is not None):
                return id_cliente
            else:
                return "Cliente no encontrado"
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
    
    def add(self, usuario_id, cliente):
        try:
            cliente_existente = self.cliente_dao.read_by_id(usuario_id)
            if cliente_existente:
                return "El cliente ya existe"
            if not self.base_repository.user_exists_and_is_role(usuario_id, "cliente"):
                return f"El usuario {usuario_id} no tiene rol cliente."
            
            nuevo_cliente = self.cliente_dao.create(usuario_id, cliente)
            return nuevo_cliente
        except Exception as e:
            print(f"Error al agregar el cliente: {e}")
            return None
        
    def update(self, usuario_id, cliente):
        try:
            cliente_existente =  self.cliente_dao.read_by_id(usuario_id)
            if not cliente_existente:
                return "Cliente no encontrado"
            self.cliente_dao.update(cliente, usuario_id)
            return "Cliente actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el cliente: {e}")
            return None
    
    def delete(self, usuario_id):
        try:
            cliente_existente = self.cliente_dao.read_by_id(usuario_id)
            if not cliente_existente:
                return "Cliente no encontrado"
            self.cliente_dao.delete(usuario_id)
            return "Cliente eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el cliente: {e}")
            return None
        
    