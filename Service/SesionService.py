from Repository.Sesion_repository import SesionRepository
from data_base.Conexion import Conexion
from Repository.Sesion_ejercicio_repository import SesionEjercicioRepository


class SesionService:
    def __init__(self, db_path: str):
        conn = Conexion(db_path).conexion
        self.conn = conn
        self.repo = SesionRepository(Conexion(db_path).conexion)
        self.repo_ej = SesionEjercicioRepository(conn)

    def add_completa(self, sesion, ejercicios):
        try:
            self.conn.execute("BEGIN")
            
            sesion_id = self.repo.add(sesion)
            if not sesion_id:
                self.conn.rollback()
                return None

            for ej in ejercicios:
                ej.sesion_id = sesion_id
                self.repo_ej.add(ej)

            self.conn.commit()
            return sesion_id

        except Exception as e:
            self.conn.rollback()
            print(f"Error en add_completa: {e}")
            return None

    def list(self): 
        return self.repo.list()
    
    def update_completa(self, sesion, ejercicios):
        try:
            self.conn.execute("BEGIN")

            ok = self.repo.update(sesion)
            if not ok:
                self.conn.rollback()
                return None

            self.repo_ej.delete_by_sesion(sesion.id)

            for ej in ejercicios:
                ej.sesion_id = sesion.id
                self.repo_ej.add(ej)

            self.conn.commit()
            return True

        except Exception as e:
            self.conn.rollback()
            print(f"Error en update_completa: {e}")
            return None
