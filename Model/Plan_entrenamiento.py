from datetime import date

class PlanEntrenamiento:
    def __init__(self, administrador_id:int, cliente_id:int, nombre: str, frecuencia: str , fecha_inicio: date, fecha_fin: date | None = None, id: int | None = None):
        self.id = id
        self.administrador_id = administrador_id
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        
    def mostrarDatos(self):
        return f"ID: {self.id}, Administrador ID: {self.administrador_id}, Cliente ID: {self.cliente_id}, Nombre: {self.nombre}, Frecuencia: {self.frecuencia}, Fecha Inicio: {self.fecha_inicio}, Fecha Fin: {self.fecha_fin}"