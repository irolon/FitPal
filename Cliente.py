from Usuario import Usuario
from datetime import date


class Cliente(Usuario):
    def __init__(self, nombre: str, apellido:str, correo: str, contrasena: str,
                dni: str, edad: int, fecha_inicio: date = None):
        super().__init__(nombre, apellido, correo, contrasena, rol="cliente")
        self.dni = dni
        self.edad = edad
        self.fecha_inicio = fecha_inicio or date.today()

    def mostrarDatos(self):
        datos_base = super().mostrarDatos()
        return f"{datos_base}, DNI: {self.dni}, Edad: {self.edad}, Fecha de Inicio: {self.fecha_inicio}"

