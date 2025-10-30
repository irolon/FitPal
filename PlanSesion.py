class PlanSesion:
    def __init__(self, id_plan: int, id_sesion: int, orden: int):
        self.id_plan = id_plan
        self.id_sesion = id_sesion
        self.orden = orden

    def __str__(self):
        return f"Plan {self.id_plan} ↔ Sesión {self.id_sesion} (Orden: {self.orden})"