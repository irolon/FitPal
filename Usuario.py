from abc import ABC, abstractmethod
from datetime import date


class Usuario(ABC):
    def __init__(self, id:int, nombre: str, apellido:str ,correo: str, contrasena: str, rol: str, fecha_alta: date, dni: int, edad: int, activo: bool):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.fecha_alta = fecha_alta
        self.dni = dni
        self.edad = edad
        self.activo = activo
        
    @abstractmethod       
    def mostrarDatos(self):
        return f"Id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido},Correo: {self.correo}, Rol: {self.rol}, Fecha de Alta: {self.fecha_alta}, DNI: {self.dni}, Edad: {self.edad}, Activo: {self.activo}"
        

