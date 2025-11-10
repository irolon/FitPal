from Repository.BaseRepository import BaseRepository
from DAO.Administrador_DAO import AdministradorDAO

class AdministradorRepository(BaseRepository):
    def __init__(self, db_connection):
        super().__init__(db_connection)
        self.administrador_dao = AdministradorDAO(db_connection)

    def get_by_id(self, administrador_id):
        try:
            id_administrador = self.administrador_dao.read_by_id(administrador_id)
            if id_administrador is not None:
                return id_administrador
            else:
                return None
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

    def add(self, administrador):
        administrador_existente = self.administrador_dao.read_by_email(administrador.correo)
        if administrador_existente:
            return "El administrador ya existe"
        try:
            administrador = self.administrador_dao.create(administrador)
            return administrador
        except Exception as e:
            print(f"Error al agregar el administrador: {e}")
            return None

    def update(self, administrador):
        try:
            administrador_existente = self.administrador_dao.read_by_id(administrador.id)
            if not administrador_existente:
                return "Administrador no encontrado"
            self.administrador_dao.update(administrador, administrador.id)
            return "Administrador actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el administrador: {e}")
            return None

    def delete(self, administrador_id):
        try:
            administrador_existente = self.administrador_dao.read_by_id(administrador_id)
            if not administrador_existente:
                return "Administrador no encontrado"
            self.administrador_dao.delete(administrador_id)
            return "Administrador eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el administrador: {e}")
            return None