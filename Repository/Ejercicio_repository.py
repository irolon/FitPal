from Repository.BaseRepository import BaseRepository
from Model.Ejercicio import Ejercicio
from DAO.Ejercicio_DAO import EjercicioDAO
from data_base.Conexion import Conexion
import sqlite3


class EjercicioRepository(BaseRepository):
    def __init__(self, db_connection: sqlite3.Connection):
        super().__init__(db_connection)
        self.dao = EjercicioDAO(db_connection)

    def crear_ejercicio(self, categoria: str, nombre: str, descripcion: str,
                        repeticiones: int, series: int, descanso: int) -> int:
        nuevo = Ejercicio(
            categoria=categoria,
            nombre=nombre,
            descripcion=descripcion,
            repeticiones=repeticiones,
            series=series,
            descanso=descanso
        )
        return self.dao.insertar(nuevo)

    def obtener_todos(self) -> list[Ejercicio]:
        return self.dao.obtener_todos()

    def obtener_por_id(self, id: int) -> Ejercicio | None:
        return self.dao.obtener_por_id(id)

    def actualizar_ejercicio(self, id: int, categoria: str, nombre: str, descripcion: str,
                             repeticiones: int, series: int, descanso: int) -> bool:
        ejercicio_existente = self.dao.obtener_por_id(id)
        if not ejercicio_existente:
            return False

        ejercicio_existente.categoria = categoria
        ejercicio_existente.nombre = nombre
        ejercicio_existente.descripcion = descripcion
        ejercicio_existente.repeticiones = repeticiones
        ejercicio_existente.series = series
        ejercicio_existente.descanso = descanso

        return self.dao.actualizar(ejercicio_existente)

    def eliminar_ejercicio(self, id: int) -> bool:
        return self.dao.eliminar(id)

    # Métodos requeridos por BaseRepository
    def get_by_id(self, entity_id: int):
        return self.obtener_por_id(entity_id)

    def list(self):
        return self.obtener_todos()

    def add(self, entity: Ejercicio):
        return self.dao.insertar(entity)

    def update(self, entity: Ejercicio) -> None:
        self.dao.actualizar(entity)

    def delete(self, entity_id: int) -> None:
        self.dao.eliminar(entity_id)
