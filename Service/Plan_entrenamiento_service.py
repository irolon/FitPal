from Model.Plan_entrenamiento import PlanEntrenamiento
from Repository.Plan_entrenamiento_repository import PlanEntrenamientoRepository
from data_base.Conexion import Conexion

class PlanEntrenamientoService:
    def __init__(self, db_path: str):
        self.repo = PlanEntrenamientoRepository(Conexion(db_path).conexion)

    def get_all(self):
        return self.repo.list()

    def get_by_id(self, plan_entrenamiento_id: int):
        return self.repo.get_by_id(plan_entrenamiento_id)

    def add(self, administrador_id: int, cliente_id: int, plan_data: dict):
        from datetime import datetime, date
        
        fecha_inicio = plan_data.get("fecha_inicio")
        if isinstance(fecha_inicio, str):
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        elif fecha_inicio is None:
            fecha_inicio = date.today()
            
        fecha_fin = plan_data.get("fecha_fin")
        if isinstance(fecha_fin, str) and fecha_fin:
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
        else:
            fecha_fin = None
        
        plan = PlanEntrenamiento(
            administrador_id=administrador_id,
            cliente_id=cliente_id,
            nombre=plan_data.get("nombre"),
            frecuencia=plan_data.get("frecuencia"),
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return self.repo.plan_entrenamiento_dao.create(
            administrador_id, cliente_id, plan
        )

    def update(self, plan_entrenamiento_id: int, plan_data: dict):
        plan_existente = self.repo.get_by_id(plan_entrenamiento_id)
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

        return self.repo.update(plan_actualizado)

    def delete(self, plan_entrenamiento_id: int):
        return self.repo.delete(plan_entrenamiento_id)

    def get_by_cliente_id(self, cliente_id: int):
        return self.repo.get_by_cliente_id(cliente_id)