
class PlanSesion:
    def __init__(self, plan_id:int, sesion_id:int, orden: int, id: int | None = None):
        self.id = id
        self.plan_id = plan_id
        self.sesion_id = sesion_id
        self.orden = orden
        
    def mostrarDatos(self):
        return f"ID: {self.id}, Plan ID: {self.plan_id}, Sesion ID: {self.sesion_id}, Orden: {self.orden}"