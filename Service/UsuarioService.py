from Repository.Usuario_repository import UsuarioRepository
from data_base import Conexion


class UsuarioService:
    def __init__(self, db_path: str):
        self.repo = UsuarioRepository(Conexion(db_path).conexion)

    def obtener_por_id(self, usuario_id: int):
        return self.repo.get_by_id(usuario_id)

    def listar(self):
        return self.repo.list()

    def crear(self, usuario):
        return self.repo.add(usuario)

    def actualizar(self, usuario):
        return self.repo.update(usuario)

    def eliminar(self, usuario_id: int):
        return self.repo.delete(usuario_id)
