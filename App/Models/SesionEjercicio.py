class SesionEjercicio:
    def __init__(self, id_sesion: int, id_ejercicio: int):
        self.id_sesion = id_sesion
        self.id_ejercicio = id_ejercicio

    def __str__(self):
        return f"Sesión {self.id_sesion} ↔ Ejercicio {self.id_ejercicio}"