from datetime import date
from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre: str, apellido: str, correo: str, contrasena: str,
                 fecha_alta: date, dni: int, edad: int, activo: bool, puntos: int = 0):
        super().__init__(nombre, apellido, correo, contrasena, rol="Cliente",
                         fecha_alta=fecha_alta, dni=dni, edad=edad, activo=activo)
        self.puntos = puntos

    def mostrarDatos(self):
        return (super().mostrarDatos() +
                f", Puntos: {self.puntos}")