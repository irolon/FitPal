from Repository.Ejercicio_repository import EjercicioRepository
from data_base.Conexion import Conexion

class EjercicioService:
    def __init__(self, db_path: str):
        self.repo = EjercicioRepository(Conexion(db_path).conexion)

    def obtener_todos(self):
        try:
            ejercicios = self.repo.obtener_todos()
            return [{"id": ej.id, "categoria": ej.categoria, "nombre": ej.nombre, 
                    "descripcion": ej.descripcion, "repeticiones": ej.repeticiones,
                    "series": ej.series, "descanso": ej.descanso} for ej in ejercicios]
        except Exception as e:
            return {"error": f"Error al obtener ejercicios: {str(e)}"}

    def obtener_por_id(self, id_ejercicio):
        try:
            ejercicio = self.repo.obtener_por_id(id_ejercicio)
            if ejercicio:
                return {"id": ejercicio.id, "categoria": ejercicio.categoria, "nombre": ejercicio.nombre,
                       "descripcion": ejercicio.descripcion, "repeticiones": ejercicio.repeticiones,
                       "series": ejercicio.series, "descanso": ejercicio.descanso}
            return {"error": "Ejercicio no encontrado"}
        except Exception as e:
            return {"error": f"Error al obtener ejercicio: {str(e)}"}

    def crear(self, categoria, nombre, descripcion, repeticiones, series, descanso, estado="Activo"):
        try:
            id_ejercicio = self.repo.crear_ejercicio(categoria, nombre, descripcion, repeticiones, series, descanso)
            return id_ejercicio
        except Exception as e:
            raise e

    def crear_ejercicio(self, categoria, nombre, descripcion, repeticiones, series, descanso):
        try:
            id_ejercicio = self.repo.crear_ejercicio(categoria, nombre, descripcion, repeticiones, series, descanso)
            return {"message": "Ejercicio creado exitosamente", "id": id_ejercicio}
        except Exception as e:
            return {"error": f"Error al crear ejercicio: {str(e)}"}

    def actualizar_ejercicio(self, id_ejercicio, categoria, nombre, descripcion, repeticiones, series, descanso):
        try:
            success = self.repo.actualizar_ejercicio(id_ejercicio, categoria, nombre, descripcion, repeticiones, series, descanso)
            if success:
                return {"message": "Ejercicio actualizado exitosamente"}
            return {"error": "No se pudo actualizar el ejercicio"}
        except Exception as e:
            return {"error": f"Error al actualizar ejercicio: {str(e)}"}

    def actualizar(self, id_ejercicio, categoria, nombre, descripcion, repeticiones, series, descanso, estado=None):
        try:
            success = self.repo.actualizar_ejercicio(id_ejercicio, categoria, nombre, descripcion, repeticiones, series, descanso)
            return success
        except Exception as e:
            raise e

    def eliminar(self, id_ejercicio):
        try:
            success = self.repo.eliminar_ejercicio(id_ejercicio)
            return success
        except Exception as e:
            raise e

    def eliminar_ejercicio(self, id_ejercicio):
        try:
            success = self.repo.eliminar_ejercicio(id_ejercicio)
            if success:
                return {"message": "Ejercicio eliminado exitosamente"}
            return {"error": "No se pudo eliminar el ejercicio"}
        except Exception as e:
            return {"error": f"Error al eliminar ejercicio: {str(e)}"}
