from Usuario import Usuario
from datetime import date


class Administrador(Usuario):
    def __init__(self, nombre: str, apellido: str, correo: str, contrasena: str,
                 activo: bool = True, fecha_alta: date = None):
        super().__init__(nombre, apellido, correo, contrasena, rol="administrador")
        self.activo = activo
        self.fecha_alta = fecha_alta 
        
        
        def permisos(self):
            return []