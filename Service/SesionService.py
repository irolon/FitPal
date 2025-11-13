from Repository.Sesion_repository import SesionRepository
from data_base.Conexion import Conexion

class SesionService:
    def __init__(self, db_path: str):
        self.repo = SesionRepository(Conexion(db_path).conexion)

    def get_by_id(self, sesion_id):
        try:
            return self.sesion_repository.get_by_id(sesion_id)
        except Exception as e:
            print(f"Error en get_by_id del servicio de Sesion: {e}")
            return None

    def list(self):
        try:
            return self.sesion_repository.list()
        except Exception as e:
            print(f"Error en list del servicio de Sesion: {e}")
            return []

    def add(self, sesion):
        try:
            return self.sesion_repository.add(sesion)
        except Exception as e:
            print(f"Error en add del servicio de Sesion: {e}")
            return None

    def update(self, sesion):
        try:
            return self.sesion_repository.update(sesion)
        except Exception as e:
            print(f"Error en update del servicio de Sesion: {e}")
            return None

    def delete(self, sesion_id):
        try:
            return self.sesion_repository.delete(sesion_id)
        except Exception as e:
            print(f"Error en delete del servicio de Sesion: {e}")
            return None
