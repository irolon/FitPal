from Repository.BaseRepository import BaseRepository
from DAO.Plan_sesion_DAO import PlanSesionDAO
import sqlite3

class PlanSesionRepository(BaseRepository):
    def __init__(self, db_connection: sqlite3.Connection):
        super().__init__(db_connection)
        self.plan_sesion_dao = PlanSesionDAO(db_connection)

    def get_by_id(self, plan_sesion_id):
        try:
            id_plan_sesion = self.plan_sesion_dao.read_by_id(plan_sesion_id)
            if id_plan_sesion is not None:
                return id_plan_sesion
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el plan de sesión por id: {e}")
            return None

    def list(self):
        try:
            planes_sesion = self.plan_sesion_dao.list()
            return planes_sesion
        except Exception as e:
            print(f"Error al listar los planes de sesión: {e}")
            return None

    def add(self, plan_sesion):
        try:
            plan_sesion = self.plan_sesion_dao.create(plan_sesion)
            return plan_sesion
        except Exception as e:
            print(f"Error al agregar el plan de sesión: {e}")
            return None
        
    def get_by_plan_id(self, plan_id):
        try:
            sesiones = self.plan_sesion_dao.read_by_plan_id(plan_id)
            return sesiones if sesiones else []
        except Exception as e:
            print(f"Error al obtener sesiones por plan_id: {e}")
            return []

    def update(self, plan_sesion):
        try:
            plan_sesion_existente = self.plan_sesion_dao.read_by_id(plan_sesion.id)
            if not plan_sesion_existente:
                return "Plan de sesión no encontrado"
            self.plan_sesion_dao.update(plan_sesion, plan_sesion.id)
            return "Plan de sesión actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el plan de sesión: {e}")
            return None

    def delete(self, plan_sesion_id):
        try:
            plan_sesion_existente = self.plan_sesion_dao.read_by_id(plan_sesion_id)
            if not plan_sesion_existente:
                return "Plan de sesión no encontrado"
            self.plan_sesion_dao.delete(plan_sesion_id)
            return "Plan de sesión eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el plan de sesión: {e}")
            return None
    
    def get_by_cliente_id(self, cliente_id):
        try:
            planes_sesion = self.plan_sesion_dao.read_by_cliente_id(cliente_id)
            return planes_sesion if planes_sesion else []
        except Exception as e:
            print(f"Error al obtener planes de sesión por cliente_id: {e}")
            return []