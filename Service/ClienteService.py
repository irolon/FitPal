from Repository.Cliente_repository import ClienteRepository
from data_base.Conexion import Conexion


class ClienteService:
    def __init__(self, db_path: str):
        self.repo = ClienteRepository(Conexion(db_path).conexion)

    def obtener_por_id(self, cliente_id: int):
        return self.repo.get_by_id(cliente_id)

    def listar(self):
        return self.repo.list()

    def crear(self, cliente):
        return self.repo.add(cliente)

    def actualizar(self, cliente):
        return self.repo.update(cliente)

    def eliminar(self, cliente_id: int):
        return self.repo.delete(cliente_id)
