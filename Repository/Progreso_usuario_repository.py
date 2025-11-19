from Repository.BaseRepository import BaseRepository
from DAO.Progreso_usuarios_DAO import ProgresoUsuariosDAO
import sqlite3

class ProgresoUsuariosRepository(BaseRepository):
    def __init__(self, db_connection: sqlite3.Connection):
        super().__init__(db_connection)
        self.progreso_usuarios_dao = ProgresoUsuariosDAO(db_connection)

    def get_by_id(self, progreso_usuario_id):
        try:
            id_progreso_usuario = self.progreso_usuarios_dao.read_by_id(progreso_usuario_id)
            if id_progreso_usuario is not None:
                return id_progreso_usuario
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el progreso del usuario por id: {e}")
            return None

    def list(self):
        try:
            progresos_usuarios = self.progreso_usuarios_dao.list()
            return progresos_usuarios
        except Exception as e:
            print(f"Error al listar los progresos de los usuarios: {e}")
            return None

    def add(self, progreso_usuario):
        try:
            progreso_usuario = self.progreso_usuarios_dao.create(progreso_usuario)
            return progreso_usuario
        except Exception as e:
            print(f"Error al agregar el progreso del usuario: {e}")
            return None

    def update(self, progreso_usuario):
        try:
            progreso_usuario_existente = self.progreso_usuarios_dao.read_by_id(progreso_usuario.id)
            if not progreso_usuario_existente:
                return "Progreso del usuario no encontrado"
            self.progreso_usuarios_dao.update(progreso_usuario, progreso_usuario.id)
            return "Progreso del usuario actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el progreso del usuario: {e}")
            return None

    def delete(self, progreso_usuario_id):
        try:
            progreso_usuario_existente = self.progreso_usuarios_dao.read_by_id(progreso_usuario_id)
            if not progreso_usuario_existente:
                return "Progreso del usuario no encontrado"
            self.progreso_usuarios_dao.delete(progreso_usuario_id)
            return "Progreso del usuario eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el progreso del usuario: {e}")
            return None