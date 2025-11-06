from Repository.BaseRepository import BaseRepository
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO

class PlanEntrenamientoRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.base_repository = BaseRepository(db_connection)
        self.plan_entrenamiento_dao = PlanEntrenamientoDAO(db_connection)

    def get_by_id(self, plan_id):
        try:
            plan = self.plan_entrenamiento_dao.read_by_id(plan_id)
            if(plan is not None):
                return plan
            else:
                return "Plan de entrenamiento no encontrado"
        except Exception as e:
            print(f"Error al obtener el plan de entrenamiento por id: {e}")
            return None
        
    def list(self):
        try:
            planes = self.plan_entrenamiento_dao.list()
            return planes
        except Exception as e:
            print(f"Error al listar los planes de entrenamiento: {e}")
            return None
    
    def add(self, plan):
        try:
            nuevo_id = self.plan_entrenamiento_dao.create(plan)
            return nuevo_id
        except Exception as e:
            print(f"Error al agregar el plan de entrenamiento: {e}")
            return None
        
    def update(self, plan_id, plan):
        try:
            plan_existente =  self.plan_entrenamiento_dao.read_by_id(plan_id)
            if not plan_existente:
                return "Plan de entrenamiento no encontrado"
            self.plan_entrenamiento_dao.update(plan, plan_id)
            return "Plan de entrenamiento actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el plan de entrenamiento: {e}")
            return None
        
    def delete(self, plan_id):
        try:
            plan_existente = self.plan_entrenamiento_dao.read_by_id(plan_id)
            if not plan_existente:
                return "Plan de entrenamiento no encontrado"
            self.plan_entrenamiento_dao.delete(plan_id)
            return "Plan de entrenamiento eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el plan de entrenamiento: {e}")
            return None