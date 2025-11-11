from Model.Plan_entrenamiento import PlanEntrenamiento
from Repository.Plan_entrenamiento_repository import PlanEntrenamientoRepository

class PlanEntrenamientoService:
    def __init__(self, db_connection):
        self.plan_entrenamiento_repository = PlanEntrenamientoRepository(db_connection)

    def list(self):
        return self.plan_entrenamiento_repository.list()

    def get_by_id(self, plan_entrenamiento_id: int):
        return self.plan_entrenamiento_repository.get_by_id(plan_entrenamiento_id)

    def add(self, administrador_id: int, cliente_id: int, plan_data: dict):
        plan = PlanEntrenamiento(
            administrador_id=administrador_id,
            cliente_id=cliente_id,
            nombre=plan_data.get("nombre"),
            frecuencia=plan_data.get("frecuencia"),
            fecha_inicio=plan_data.get("fecha_inicio"),
            fecha_fin=plan_data.get("fecha_fin")
        )
        return self.plan_entrenamiento_repository.plan_entrenamiento_dao.create(
            administrador_id, cliente_id, plan
        )

    def update(self, plan_entrenamiento_id: int, plan_data: dict):
        plan_existente = self.plan_entrenamiento_repository.get_by_id(plan_entrenamiento_id)
        if not plan_existente:
            return "Plan de entrenamiento no encontrado"

        plan_actualizado = PlanEntrenamiento(
            administrador_id=plan_existente.administrador_id,
            cliente_id=plan_existente.cliente_id,
            nombre=plan_data.get("nombre", plan_existente.nombre),
            frecuencia=plan_data.get("frecuencia", plan_existente.frecuencia),
            fecha_inicio=plan_data.get("fecha_inicio", plan_existente.fecha_inicio),
            fecha_fin=plan_data.get("fecha_fin", plan_existente.fecha_fin),
            id=plan_entrenamiento_id
        )

        return self.plan_entrenamiento_repository.update(plan_actualizado)

    def delete(self, plan_entrenamiento_id: int):
        return self.plan_entrenamiento_repository.delete(plan_entrenamiento_id)
