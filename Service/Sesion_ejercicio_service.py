from Repository.Sesion_ejercicio_repository import SesionEjercicioRepository
from DAO.Sesion_ejercicio_DAO import SesionEjercicioDAO
from data_base.Conexion import Conexion

class SesionEjercicioService:
    def __init__(self, db_path: str):
        conn = Conexion(db_path).conexion
        self.repo = SesionEjercicioRepository(conn)

    def obtener_todos(self):
        return self.repo.list()

    def obtener_por_id(self, sesion_ejercicio_id):
        return self.repo.get_by_id(sesion_ejercicio_id)

    def crear(self, sesion_ejercicio):
        return self.repo.add(sesion_ejercicio)

    def actualizar(self, sesion_ejercicio):
        return self.repo.update(sesion_ejercicio)

    def eliminar(self, sesion_ejercicio_id):
        return self.repo.delete(sesion_ejercicio_id)

    def obtener_ejercicios_por_sesion(self, sesion_id):
        return self.repo.obtener_por_sesion(sesion_id)
