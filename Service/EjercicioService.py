from data_base.Conexion import Conexion
from Repository.Ejercicio_repository import EjercicioRepository

class EjercicioService:
    def __init__(self, db_path: str = "data_base/db_fitpal.db"):
        self.repo = EjercicioRepository(db_path)

    def obtener_todos(self):
        return self.repository.obtener_todos()

    def obtener_por_id(self, id_ejercicio):
        return self.repository.obtener_por_id(id_ejercicio)

    def crear(self, datos):
        return self.repository.crear(datos)

    def actualizar(self, id_ejercicio, datos):
        return self.repository.actualizar(id_ejercicio, datos)

    def eliminar(self, id_ejercicio):
        return self.repository.eliminar(id_ejercicio)
