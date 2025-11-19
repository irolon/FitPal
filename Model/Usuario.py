from abc import ABC


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, correo: str, contrasena: str, rol: str, id: int | None = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        

    def mostrarDatos(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.correo}, Rol: {self.rol}, ID: {self.id}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'rol': self.rol
        }

