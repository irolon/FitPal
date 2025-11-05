from Repository.BaseRepository import BaseRepository
from DAO.Administrador_DAO import AdministradorDAO

class AdministradorRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.base_repository = BaseRepository(db_connection)
        self.administrador_dao = AdministradorDAO(db_connection)

    def get_by_id(self, usuario_id):
        try:
            id_administrador = self.administrador_dao.read_by_id(usuario_id)
            if(id_administrador is not None):
                return id_administrador
            else:
                return "Administrador no encontrado"
        except Exception as e:
            print(f"Error al obtener el administrador por id: {e}")
            return None
        
    def list(self):
        try:
            administradores = self.administrador_dao.list()
            return administradores
        except Exception as e:
            print(f"Error al listar los administradores: {e}")
            return None
    
    def add(self, usuario_id, administrador):
        try:
            administrador_existente = self.administrador_dao.read_by_id(usuario_id)
            if administrador_existente:
                return "El administrador ya existe"
            if administrador_existente[0] != "administrador":
                return f"El usuario {usuario_id} no tiene rol administrador."
            
            nuevo_admin = self.administrador_dao.create(usuario_id, administrador)
            return nuevo_admin
        except Exception as e:
            print(f"Error al agregar el administrador: {e}")
            return None
        
    def update(self, usuario_id, administrador):
        try:
            administrador_existente =  self.administrador_dao.read_by_id(usuario_id)
            if not administrador_existente:
                return "Administrador no encontrado"
            self.administrador_dao.update(administrador, usuario_id)
            return "Administrador actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el administrador: {e}")
            return None
        
    def delete(self, usuario_id):
        try:
            administrador_existente = self.administrador_dao.read_by_id(usuario_id)
            if not administrador_existente:
                return "Administrador no encontrado"
            self.administrador_dao.delete(usuario_id)
            return "Administrador eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el administrador: {e}")
            return None


    