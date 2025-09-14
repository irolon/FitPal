from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido:str ,correo: str, contrasena: str, rol: str):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        
            
    def mostrarDatos(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Rol: {self.rol}"
        

    @abstractmethod
    def permisos(self):
        pass