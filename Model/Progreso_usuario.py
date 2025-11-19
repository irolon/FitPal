class ProgresoUsuario:
    def __init__(self, usuario_id:int, logro_id:int, fecha_logro:str, puntaje:int, nivel:int, id: int | None = None):
        self.id = id
        self.usuario_id = usuario_id
        self.logro_id = logro_id
        self.fecha_logro = fecha_logro
        self.puntaje = puntaje
        self.nivel = nivel
        
    
    def mostrarDatos(self):
        return f"ID: {self.id}, Usuario ID: {self.usuario_id}, Logro ID: {self.logro_id}, Fecha Logro: {self.fecha_logro}, Puntaje: {self.puntaje}, Nivel: {self.nivel}"
        