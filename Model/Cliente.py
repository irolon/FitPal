from Model.Usuario import Usuario
from datetime import date


class Cliente(Usuario):
    def __init__(self, nombre:str, apellido:str, correo:str, contrasena:str,
                 dni:str, edad:int, fecha_inicio: date | None = None,
                 id: int | None = None, rol: str = "cliente"):
        super().__init__(nombre, apellido, correo, contrasena, rol, id=id)
        self.dni = dni
        self.edad = edad
        self.fecha_inicio = fecha_inicio or date.today()

    @classmethod
    def from_usuario(cls, usuario: Usuario, dni: str, edad: int, fecha_inicio=None):
        return cls(usuario.nombre, usuario.apellido, usuario.correo, usuario.contrasena,
                   dni, edad, fecha_inicio, id=usuario.id, rol=usuario.rol)
    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'dni': self.dni,
            'edad': self.edad,
            'fecha_inicio': self.fecha_inicio.isoformat() if self.fecha_inicio else None
        })
        return base_dict