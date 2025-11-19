class Logros:
    def __init__(self, tipo:str, descripcion:str, id: int | None = None):
        self.id = id
        self.tipo = tipo
        self.descripcion = descripcion
        
    def mostrarDatos(self):
        return f"ID: {self.id}, Tipo: {self.tipo}, Descripción: {self.descripcion}"