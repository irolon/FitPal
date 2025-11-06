from Repository.BaseRepository import BaseRepository
from DAO.Usuario_DAO import UsuarioDAO
import sqlite3

class UsuarioRepository(BaseRepository):
    def __init__(self, db_connection: sqlite3.Connection):
        super().__init__(db_connection)
        self.usuario_dao = UsuarioDAO(db_connection)
        
    def get_by_id(self, usuario_id: int):
        try:
            id_usuario = self.usuario_dao.read_by_id(usuario_id)
            if id_usuario is not None:
                return id_usuario
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el usuario por id: {e}")
            return None

            
    def list(self):
        try:
            usuarios = self.usuario_dao.list()
            return usuarios
        except Exception as e:
            print(f"Error al listar los usuarios: {e}")
            return None

            
    def add(self, usuario):
        usuario_existente = self.usuario_dao.read_by_email(usuario.correo)
        if usuario_existente:
            return "El usuario ya existe"
        try:
            usuario = self.usuario_dao.create(usuario)
            return usuario
        except Exception as e:
            print(f"Error al agregar el usuario: {e}")
            return None

            
    def update(self, usuario):
        try:
            usuario_existente = self.usuario_dao.read_by_id(usuario.id)
            if not usuario_existente:
                return "Usuario no encontrado"
            self.usuario_dao.update(usuario, usuario.id)
            return "Usuario actualizado con éxito"
        except Exception as e:
            print(f"Error al actualizar el usuario: {e}")
            return None

            
    def delete(self, usuario_id: int):
        try:
            usuario_existente = self.usuario_dao.read_by_id(usuario_id)
            if not usuario_existente:
                return "Usuario no encontrado"
            self.usuario_dao.delete(usuario_id)
            return "Usuario eliminado con éxito"
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
            return None

            
    
