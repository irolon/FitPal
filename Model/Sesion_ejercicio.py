class SesionEjercicio:
    def __init__(self, sesion_id: int, ejercicio_id: int, orden:int, id: int | None = None):
        self.id = id
        self.sesion_id = sesion_id
        self.ejercicio_id = ejercicio_id
        self.orden = orden

    def mostrarDatos(self):
        return f"ID: {self.id}, Sesion ID: {self.sesion_id}, Ejercicio ID: {self.ejercicio_id}, Orden: {self.orden}"