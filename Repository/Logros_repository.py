from Repository.BaseRepository import BaseRepository
from DAO.Logros_DAO import LogrosDAO
import sqlite3

class LogrosRepository(BaseRepository):
    def __init__(self, db_connection: sqlite3.Connection):
        super().__init__(db_connection)
        self.logros_dao = LogrosDAO(db_connection)
        
    def get_by_id(self, logro_id):
        try:
            logro = self.logros_dao.read_by_id(logro_id)
            if logro is not None:
                return logro
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el logro por id: {e}")
            return None
    
    def list(self):
        try:
            logros = self.logros_dao.list()
            return logros
        except Exception as e:
            print(f"Error al listar los logros: {e}")
            return None
        
    def add(self, logro):
        try:
            logro = self.logros_dao.create(logro)
            return logro
        except Exception as e:
            print(f"Error al agregar el logro: {e}")
            return None
        
    def update(self, logro):
        try:
            logro_existente = self.logros_dao.read_by_id(logro.id)
            if not logro_existente:
                return "Logro no encontrado"
            self.logros_dao.update(logro, logro.id)
            return "Logro actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el logro: {e}")
            return None
        
    def delete(self, logro_id):
        try:
            logro_existente = self.logros_dao.read_by_id(logro_id)
            if not logro_existente:
                return "Logro no encontrado"
            self.logros_dao.delete(logro_id)
            return "Logro eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el logro: {e}")
            return None