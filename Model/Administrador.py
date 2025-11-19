from Model.Usuario import Usuario
from datetime import date


class Administrador(Usuario):
    def __init__(self, nombre: str, apellido: str, correo: str, contrasena: str,
                 activo: bool, fecha_alta: date = None):
        super().__init__(nombre, apellido, correo, contrasena, rol="administrador")
        self.activo = activo
        self.fecha_alta = fecha_alta or date.today() 
        
        

    @classmethod
    def from_usuario(cls, usuario: Usuario, activo: bool, fecha_alta: date = None):
        return cls(usuario.nombre, usuario.apellido, usuario.correo, usuario.contrasena,
                   activo, fecha_alta)
        