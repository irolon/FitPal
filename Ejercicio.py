class Ejercicio:
    def __init__(self, id: int, categoria: str, nombre: str,
                 series: int = None, repeticiones: int = None, tiempo: int = None):
        self.id = id
        self.categoria = categoria
        self.nombre = nombre
        self.series = series
        self.repeticiones = repeticiones
        self.tiempo = tiempo

    def __str__(self):
        detalles = f"ID: {self.id}, Categoría: {self.categoria}, Nombre: {self.nombre}"
        if self.series:
            detalles += f", Series: {self.series}"
        if self.repeticiones:
            detalles += f", Repeticiones: {self.repeticiones}"
        if self.tiempo:
            detalles += f", Tiempo: {self.tiempo} seg"
        return detalles
