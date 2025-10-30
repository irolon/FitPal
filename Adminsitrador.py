from Usuario import Usuario
from datetime import date


class Administrador(Usuario):
    def __init__(self, id:int, nombre: str, apellido: str, correo: str, contrasena: str,
                 fecha_alta: date, dni: int, edad: int, activo: bool, nivel_acceso: int = 1):
        super().__init__(nombre, apellido, correo, contrasena, rol="Administrador",
                         fecha_alta=fecha_alta, dni=dni, edad=edad, activo=activo)
        self.nivel_acceso = nivel_acceso

    def mostrarDatos(self):
        return (super().mostrarDatos() +
                f", Nivel de acceso: {self.nivel_acceso}")