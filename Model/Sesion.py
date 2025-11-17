
class Sesion:
    def __init__(self, nombre: str, descripcion: str, id: int | None = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = False
        
        
        
    def mostrarDatos(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Descripción: {self.descripcion}, Estado: {self.estado}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'estado': self.estado
        }