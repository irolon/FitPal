from Repository.Sesion_ejercicio_repository import SesionEjercicioRepository
from DAO.Sesion_ejercicio_DAO import SesionEjercicioDAO
from data_base.Conexion import Conexion

class SesionEjercicioService:
    def __init__(self, db_path: str):
        self.conexion = Conexion(db_path)
        self.repo = SesionEjercicioRepository(self.conexion.conexion)
        self.dao = SesionEjercicioDAO(self.conexion.conexion)

    def obtener_todos(self):
        return self.repo.list()

    def obtener_por_id(self, sesion_ejercicio_id):
        return self.repo.get_by_id(sesion_ejercicio_id)

    def crear(self, sesion_ejercicio):
        return self.repo.add(sesion_ejercicio)

    def actualizar(self, sesion_ejercicio):
        return self.repo.update(sesion_ejercicio)

    def eliminar(self, sesion_ejercicio_id):
        return self.repo.delete(sesion_ejercicio_id)
    
    def obtener_ejercicios_por_sesion(self, sesion_id):
        """Obtiene todos los ejercicios de una sesión específica"""
        try:
            return self.dao.get_ejercicios_por_sesion(sesion_id)
        except Exception as e:
            print(f"Error en obtener_ejercicios_por_sesion: {e}")
            return []
    
    def obtener_ejercicios_por_cliente(self, cliente_id):
        """Obtiene todos los ejercicios asignados a un cliente"""
        try:
            return self.dao.get_ejercicios_por_cliente(cliente_id)
        except Exception as e:
            print(f"Error en obtener_ejercicios_por_cliente: {e}")
            return []
