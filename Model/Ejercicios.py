class Ejercicio:
    def __init__(self, categoria: str, nombre:str, descripcion:str, repeticiones:int, series:int, descanso:int, id: int | None = None):
        self.id = id
        self.categoria = categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.repeticiones = repeticiones
        self.series = series
        self.descanso = descanso

    def mostrarDatos(self):
        return f"ID: {self.id}, Categoria: {self.categoria}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Repeticiones: {self.repeticiones}, Series: {self.series}, Descanso: {self.descanso}"