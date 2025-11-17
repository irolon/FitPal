from Repository.Sesion_repository import SesionRepository
from data_base.Conexion import Conexion

class SesionService:
    def __init__(self, db_path: str):
        self.repo = SesionRepository(Conexion(db_path).conexion)

    def get_by_id(self, sesion_id):
        try:
            return self.repo.get_by_id(sesion_id)
        except Exception as e:
            print(f"Error en get_by_id del servicio de Sesion: {e}")
            return None

    def list(self):
        try:
            return self.repo.list()
        except Exception as e:
            print(f"Error en list del servicio de Sesion: {e}")
            return []

    def add(self, sesion):
        try:
            return self.repo.add(sesion)
        except Exception as e:
            print(f"Error en add del servicio de Sesion: {e}")
            return None

    def update(self, sesion):
        try:
            return self.repo.update(sesion)
        except Exception as e:
            print(f"Error en update del servicio de Sesion: {e}")
            return None

    def delete(self, sesion_id):
        try:
            return self.repo.delete(sesion_id)
        except Exception as e:
            print(f"Error en delete del servicio de Sesion: {e}")
            return None

    def obtener_por_cliente_id(self, cliente_id):
        try:
            return self.repo.obtener_por_cliente_id(cliente_id)
        except Exception as e:
            print(f"Error en obtener_por_cliente_id del servicio de Sesion: {e}")
            return None
    
    def actualizar_estado(self, sesion_id, estado):
        try:
            return self.repo.actualizar_estado(sesion_id, estado)
        except Exception as e:
            print(f"Error en actualizar_estado del servicio de Sesion: {e}")
            return False