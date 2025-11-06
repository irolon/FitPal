from Repository.BaseRepository import BaseRepository
from DAO.Plan_sesion_DAO import PlanSesionDAO

class PlanSesionRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.base_repository = BaseRepository(db_connection)
        self.plan_sesion_dao = PlanSesionDAO(db_connection)
        
    def get_by_id(self, plan_id):
        try:
            plan = self.plan_sesion_dao.read_by_id(plan_id)
            if(plan is not None):
                return plan
            else:
                return "Plan de sesión no encontrado"
        except Exception as e:
            print(f"Error al obtener el plan de sesión por id: {e}")
            return None
        
    def list(self):
        try:
            planes = self.plan_sesion_dao.list()
            return planes
        except Exception as e:
            print(f"Error al listar los planes de sesión: {e}")
            return None
    
    def add(self, plan):
        try:
            nuevo_id = self.plan_sesion_dao.create(plan)
            return nuevo_id
        except Exception as e:
            print(f"Error al agregar el plan de sesión: {e}")
            return None
    
    def update(self, plan_id, plan):
        try:
            plan_existente =  self.plan_sesion_dao.read_by_id(plan_id)
            if not plan_existente:
                return "Plan de sesión no encontrado"
            self.plan_sesion_dao.update(plan, plan_id)
            return "Plan de sesión actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el plan de sesión: {e}")
            return None
        
    def delete(self, plan_id):
        try:
            plan_existente = self.plan_sesion_dao.read_by_id(plan_id)
            if not plan_existente:
                return "Plan de sesión no encontrado"
            self.plan_sesion_dao.delete(plan_id)
            return "Plan de sesión eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el plan de sesión: {e}")
            return None
        
    