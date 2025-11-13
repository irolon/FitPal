from Repository.Administrador_respository import AdministradorRepository
from data_base.Conexion import Conexion


class AdministradorService:
    def __init__(self, db_path: str):
        self.repo = AdministradorRepository(Conexion(db_path).conexion)

    def obtener_por_id(self, admin_id: int):
        return self.repo.get_by_id(admin_id)

    def listar(self):
        return self.repo.list()

    def crear(self, admin):
        return self.repo.add(admin)

    def actualizar(self, admin):
        return self.repo.update(admin)

    def eliminar(self, admin_id: int):
        return self.repo.delete(admin_id)
