from Usuario import Usuario
from datetime import date


class Cliente(Usuario):
     def __init__(self, nombre: str, correo: str, contrasena: str, rol: str,
                 dni: str, edad: int,  fecha_inicio: date = None):
        super().__init__(nombre, correo, contrasena, rol = "cliente")
        self.dni = dni
        self.edad = edad
        self.fecha_inicio = fecha_inicio


        def permisos(self):
            return []
    
    
