from Repository.Ejercicio_repository import EjercicioRepository
from Model.Ejercicio import Ejercicio

class EjercicioService:
    def __init__(self, db_path: str = "fitpal.db"):
        self.repository = EjercicioRepository(db_path)

    def crear_ejercicio(self, categoria: str, nombre: str, descripcion: str,
                        repeticiones: int, series: int, descanso: int) -> dict:
        # Validaciones básicas
        if not categoria or not nombre:
            return {"error": "La categoría y el nombre son obligatorios."}

        if repeticiones <= 0 or series <= 0:
            return {"error": "Las repeticiones y las series deben ser mayores a cero."}

        if descanso < 0:
            return {"error": "El tiempo de descanso no puede ser negativo."}

        ejercicio_id = self.repository.crear_ejercicio(
            categoria=categoria,
            nombre=nombre,
            descripcion=descripcion,
            repeticiones=repeticiones,
            series=series,
            descanso=descanso
        )
        return {"mensaje": "Ejercicio creado correctamente.", "id": ejercicio_id}

    def obtener_todos(self) -> list[dict]:
        ejercicios = self.repository.obtener_todos()
        return [
            {
                "id": e.id,
                "categoria": e.categoria,
                "nombre": e.nombre,
                "descripcion": e.descripcion,
                "repeticiones": e.repeticiones,
                "series": e.series,
                "descanso": e.descanso
            }
            for e in ejercicios
        ]

    def obtener_por_id(self, id: int) -> dict:
        ejercicio = self.repository.obtener_por_id(id)
        if not ejercicio:
            return {"error": "Ejercicio no encontrado."}

        return {
            "id": ejercicio.id,
            "categoria": ejercicio.categoria,
            "nombre": ejercicio.nombre,
            "descripcion": ejercicio.descripcion,
            "repeticiones": ejercicio.repeticiones,
            "series": ejercicio.series,
            "descanso": ejercicio.descanso
        }

    def actualizar_ejercicio(self, id: int, categoria: str, nombre: str, descripcion: str,
                             repeticiones: int, series: int, descanso: int) -> dict:
        if repeticiones <= 0 or series <= 0:
            return {"error": "Las repeticiones y las series deben ser mayores a cero."}

        actualizado = self.repository.actualizar_ejercicio(
            id=id,
            categoria=categoria,
            nombre=nombre,
            descripcion=descripcion,
            repeticiones=repeticiones,
            series=series,
            descanso=descanso
        )

        if not actualizado:
            return {"error": "No se pudo actualizar el ejercicio (posiblemente no existe)."}
        return {"mensaje": "Ejercicio actualizado correctamente."}

    def eliminar_ejercicio(self, id: int) -> dict:
        eliminado = self.repository.eliminar_ejercicio(id)
        if not eliminado:
            return {"error": "No se pudo eliminar el ejercicio (posiblemente no existe)."}
        return {"mensaje": "Ejercicio eliminado correctamente."}
