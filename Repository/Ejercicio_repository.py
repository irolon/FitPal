from Model.Ejercicio import Ejercicio
from DAO.Ejercicio_DAO import Ejercicio_DAO

class EjercicioRepository:
    def __init__(self, db_path: str = "fitpal.db"):
        self.dao = Ejercicio_DAO(db_path)

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
