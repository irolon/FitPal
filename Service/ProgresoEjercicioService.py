from DAO.Progreso_ejercicio_DAO import ProgresoEjercicioDAO
from data_base.Conexion import Conexion

class ProgresoEjercicioService:
    def __init__(self, db_path: str):
        self.conexion = Conexion(db_path)
        self.dao = ProgresoEjercicioDAO(self.conexion.conexion)
        self.dao.create_table()

    def obtener_progreso_cliente(self, cliente_id: int):
        try:
            return self.dao.obtener_progreso_por_cliente(cliente_id)
        except Exception as e:
            print(f"Error en obtener_progreso_cliente: {e}")
            return {}

    def actualizar_estado_ejercicio(self, cliente_id: int, ejercicio_id: int, nuevo_estado: str):
        try:
            if nuevo_estado not in ['pendiente', 'completado']:
                return {"error": "Estado inválido. Use 'pendiente' o 'completado'"}
            
            resultado = self.dao.actualizar_estado_ejercicio(cliente_id, ejercicio_id, nuevo_estado)
            if resultado:
                return {"message": f"Estado actualizado a {nuevo_estado}", "success": True}
            else:
                return {"error": "No se pudo actualizar el estado"}
        except Exception as e:
            print(f"Error en actualizar_estado_ejercicio: {e}")
            return {"error": str(e)}