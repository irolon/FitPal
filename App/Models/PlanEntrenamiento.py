from datetime import date

class PlanEntrenamiento:
    def __init__(self, id_admin: int, id_cliente: int,
                 nombre: str, frecuencia: str, fecha_inicio: date, fecha_fin: date):
        self.id_admin = id_admin
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        return (f"Plan {self.id}: {self.nombre} | Admin ID: {self.id_admin} | "
                f"Cliente ID: {self.id_cliente} | Frecuencia: {self.frecuencia} | "
                f"Inicio: {self.fecha_inicio} | Fin: {self.fecha_fin}")