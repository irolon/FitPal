from Repository.BaseRepository import BaseRepository
from DAO.Sesiones_DAO import SesionesDAO

class SesionRepository(BaseRepository):
    def __init__(self, db_connection):
        super().__init__(db_connection)
        self.sesiones_dao = SesionesDAO(db_connection)

    def get_by_id(self, sesion_id):
        try:
            id_sesion = self.sesiones_dao.read_by_id(sesion_id)
            if id_sesion is not None:
                return id_sesion
            else:
                return None
        except Exception as e:
            print(f"Error al obtener la sesión por id: {e}")
            return None

    def list(self):
        try:
            sesiones = self.sesiones_dao.list()
            return sesiones
        except Exception as e:
            print(f"Error al listar las sesiones: {e}")
            return None

    def add(self, sesion):
        try:
            sesion = self.sesiones_dao.create(sesion)
            return sesion
        except Exception as e:
            print(f"Error al agregar la sesión: {e}")
            return None

    def update(self, sesion):
        try:
            sesion_existente = self.sesiones_dao.read_by_id(sesion.id)
            if not sesion_existente:
                return "Sesión no encontrada"
            self.sesiones_dao.update(sesion, sesion.id)
            return "Sesión actualizada con éxito"
        except Exception as e:
            print(f"Error al actualizar la sesión: {e}")
            return None

    def delete(self, sesion_id):
        try:
            sesion_existente = self.sesiones_dao.read_by_id(sesion_id)
            if not sesion_existente:
                return "Sesión no encontrada"
            self.sesiones_dao.delete(sesion_id)
            return "Sesión eliminada con éxito"
        except Exception as e:
            print(f"Error al eliminar la sesión: {e}")
            return None