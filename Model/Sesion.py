
class Sesion:
    def __init__(self, nombre: str, id: int | None = None):
        self.id = id
        self.nombre = nombre
        
    def mostrarDatos(self):
        return f"Nombre: {self.nombre}, ID: {self.id}"