from Repository.BaseRepository import BaseRepository
from DAO.Sesion_ejercicio_DAO import SesionEjercicioDAO
import sqlite3

class SesionEjercicioRepository(BaseRepository):
    def __init__(self, db_connection: sqlite3.Connection):
        super().__init__(db_connection)
        self.sesion_ejercicio_dao = SesionEjercicioDAO(db_connection)

    def get_by_id(self, sesion_ejercicio_id):
        try:
            id_sesion_ejercicio = self.sesion_ejercicio_dao.read_by_id(sesion_ejercicio_id)
            if id_sesion_ejercicio is not None:
                return id_sesion_ejercicio
            else:
                return None
        except Exception as e:
            print(f"Error al obtener la sesión de ejercicio por id: {e}")
            return None

    def list(self):
        try:
            sesiones_ejercicio = self.sesion_ejercicio_dao.list()
            return sesiones_ejercicio
        except Exception as e:
            print(f"Error al listar las sesiones de ejercicio: {e}")
            return None

    def add(self, sesion_ejercicio):
        try:
            sesion_ejercicio = self.sesion_ejercicio_dao.create(sesion_ejercicio)
            return sesion_ejercicio
        except Exception as e:
            print(f"Error al agregar la sesión de ejercicio: {e}")
            return None

    def update(self, sesion_ejercicio):
        try:
            sesion_ejercicio_existente = self.sesion_ejercicio_dao.read_by_id(sesion_ejercicio.id)
            if not sesion_ejercicio_existente:
                return "Sesión de ejercicio no encontrada"
            self.sesion_ejercicio_dao.update(sesion_ejercicio, sesion_ejercicio.id)
            return "Sesión de ejercicio actualizada con éxito"
        except Exception as e:
            print(f"Error al actualizar la sesión de ejercicio: {e}")
            return None

    def obtener_por_sesion(self, sesion_id):
        try:
            return self.sesion_ejercicio_dao.obtener_por_sesion(sesion_id)
        except Exception as e:
            print(f"Error al obtener ejercicios por sesión: {e}")
            return []

    def delete_by_sesion(self, sesion_id):
        try:
            self.sesion_ejercicio_dao.delete_by_sesion(sesion_id)
        except Exception as e:
            print(f"Error al borrar ejercicios de la sesión: {e}")

    def delete(self, sesion_ejercicio_id):
        try:
            # Usamos el DAO para borrar por id
            self.sesion_ejercicio_dao.delete(sesion_ejercicio_id)
            return "Sesión de ejercicio eliminada con éxito"
        except Exception as e:
            print(f"Error al eliminar la sesión de ejercicio: {e}")
            return None

    def agregar_ejercicio(self, sesion_id, ejercicio_id):
        try:
            return self.sesion_ejercicio_dao.agregar_ejercicio(sesion_id, ejercicio_id)
        except Exception as e:
            print(f"Error al agregar ejercicio a la sesión: {e}")
            return None

    def eliminar_ejercicio(self, sesion_id, ejercicio_id):
        try:
            return self.sesion_ejercicio_dao.eliminar_ejercicio(sesion_id, ejercicio_id)
        except Exception as e:
            print(f"Error al eliminar ejercicio de la sesión: {e}")
            return None

    def get_ejercicios_por_cliente(self, cliente_id):
        try:
            return self.sesion_ejercicio_dao.get_ejercicios_por_cliente(cliente_id)
        except Exception as e:
            print(f"Error al obtener ejercicios por cliente: {e}")
            return []