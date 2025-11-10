from Repository.BaseRepository import BaseRepository
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO

class PlanEntrenamientoRepository(BaseRepository):
    def __init__(self, db_connection):
        super().__init__(db_connection)
        self.plan_entrenamiento_dao = PlanEntrenamientoDAO(db_connection)
        
    def get_by_id(self, plan_entrenamiento_id):
        try:
            id_plan_entrenamiento = self.plan_entrenamiento_dao.read_by_id(plan_entrenamiento_id)
            if id_plan_entrenamiento is not None:
                return id_plan_entrenamiento
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el plan de entrenamiento por id: {e}")
            return None
    
    def list(self):
        try:
            planes_entrenamiento = self.plan_entrenamiento_dao.list()
            return planes_entrenamiento
        except Exception as e:
            print(f"Error al listar los planes de entrenamiento: {e}")
            return None
        
    def add(self, plan_entrenamiento):
        try:
            plan_entrenamiento = self.plan_entrenamiento_dao.create(plan_entrenamiento)
            return plan_entrenamiento
        except Exception as e:
            print(f"Error al agregar el plan de entrenamiento: {e}")
            return None
        
    def update(self, plan_entrenamiento):
        try:
            plan_entrenamiento_existente = self.plan_entrenamiento_dao.read_by_id(plan_entrenamiento.id)
            if not plan_entrenamiento_existente:
                return "Plan de entrenamiento no encontrado"
            self.plan_entrenamiento_dao.update(plan_entrenamiento, plan_entrenamiento.id)
            return "Plan de entrenamiento actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el plan de entrenamiento: {e}")
            return None
        
    def delete(self, plan_entrenamiento_id):
        try:
            plan_entrenamiento_existente = self.plan_entrenamiento_dao.read_by_id(plan_entrenamiento_id)
            if not plan_entrenamiento_existente:
                return "Plan de entrenamiento no encontrado"
            self.plan_entrenamiento_dao.delete(plan_entrenamiento_id)
            return "Plan de entrenamiento eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el plan de entrenamiento: {e}")
            return None
        