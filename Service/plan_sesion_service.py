from Repository.Plan_sesion_repository import PlanSesionRepository
from data_base.Conexion import Conexion

class PlanSesionService:
    def __init__(self, db_path: str):
        self.repo = PlanSesionRepository(Conexion(db_path).conexion)

    def obtener_todos(self):
        return self.repo.list()

    def obtener_por_id(self, plan_sesion_id):
        return self.repo.get_by_id(plan_sesion_id)

    def crear(self, plan_sesion):
        return self.repo.add(plan_sesion)

    def actualizar(self, plan_sesion):
        return self.repo.update(plan_sesion)

    def eliminar(self, plan_sesion_id):
        return self.repo.delete(plan_sesion_id)
    
    def obtener_por_cliente_id(self, cliente_id):
        return self.repo.get_by_cliente_id(cliente_id)
