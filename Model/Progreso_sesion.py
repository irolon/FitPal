class ProgresoSesion:
    def __init__(self, cliente_id: int, sesion_id: int, estado: bool = False, fecha_completado: str = None, id: int = None):
        self.id = id
        self.cliente_id = cliente_id
        self.sesion_id = sesion_id
        self.estado = estado
        self.fecha_completado = fecha_completado
        
    def to_dict(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'sesion_id': self.sesion_id,
            'estado': self.estado,
            'fecha_completado': self.fecha_completado
        }
    
    def mostrarDatos(self):
        return f"Cliente: {self.cliente_id}, Sesión: {self.sesion_id}, Estado: {self.estado}, Fecha: {self.fecha_completado}"