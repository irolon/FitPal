class Sesion:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return f"Sesión {self.id}: {self.nombre}"