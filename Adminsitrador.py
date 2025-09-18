from Usuario import Usuario
from datetime import date


class Administrador(Usuario):
    def __init__(self, nombre: str, apellido: str, correo: str, contrasena: str,
                 activo: bool, fecha_alta: date = None):
        super().__init__(nombre, apellido, correo, contrasena, rol="administrador")
        self.activo = activo
        self.fecha_alta = fecha_alta or date.today() 
        
        
    def mostrarDatos(self):
        datos_base = super().mostrarDatos()
        estado = "Activo" if self.activo else "Inactivo"
        return f"{ datos_base}, Estado: {estado}, Fecha de Alta: {self.fecha_alta}"