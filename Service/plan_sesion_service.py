from Repository.Plan_sesion_repository import PlanSesionRepository

class PlanSesionService:
    def __init__(self, db_connection):
        self.repository = PlanSesionRepository(db_connection)

    def obtener_todos(self):
        return self.repository.list()

    def obtener_por_id(self, plan_sesion_id):
        return self.repository.get_by_id(plan_sesion_id)

    def crear(self, plan_sesion):
        return self.repository.add(plan_sesion)

    def actualizar(self, plan_sesion):
        return self.repository.update(plan_sesion)

    def eliminar(self, plan_sesion_id):
        return self.repository.delete(plan_sesion_id)
