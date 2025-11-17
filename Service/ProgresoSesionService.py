from DAO.Progreso_sesion_DAO import ProgresoSesionDAO
from data_base.Conexion import Conexion

class ProgresoSesionService:
    def __init__(self, db_path: str):
        conexion = Conexion(db_path)
        self.dao = ProgresoSesionDAO(conexion.conexion)
        self.dao.create_table()

    def obtener_sesiones_con_progreso_cliente(self, cliente_id: int):
        try:
            return self.dao.obtener_sesiones_con_progreso_por_cliente(cliente_id)
        except Exception as e:
            print(f"Error en obtener_sesiones_con_progreso_cliente: {e}")
            return []

    def actualizar_progreso_sesion(self, cliente_id: int, sesion_id: int, estado: bool):
        try:
            return self.dao.actualizar_o_crear_progreso(cliente_id, sesion_id, estado)
        except Exception as e:
            print(f"Error en actualizar_progreso_sesion: {e}")
            return False