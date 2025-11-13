from Repository.Sesion_ejercicio_repository import SesionEjercicioRepository
from data_base.Conexion import Conexion

class SesionEjercicioService:
    def __init__(self, db_path: str):
        self.repo = SesionEjercicioRepository(Conexion(db_path).conexion)

    def obtener_todos(self):
        return self.repository.list()

    def obtener_por_id(self, sesion_ejercicio_id):
        return self.repository.get_by_id(sesion_ejercicio_id)

    def crear(self, sesion_ejercicio):
        return self.repository.add(sesion_ejercicio)

    def actualizar(self, sesion_ejercicio):
        return self.repository.update(sesion_ejercicio)

    def eliminar(self, sesion_ejercicio_id):
        return self.repository.delete(sesion_ejercicio_id)
