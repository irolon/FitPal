from Repository.Sesion_ejercicio_repository import SesionEjercicioRepository

class SesionEjercicioService:
    def __init__(self, db_connection):
        self.sesion_ejercicio_repository = SesionEjercicioRepository(db_connection)

    def get_by_id(self, sesion_ejercicio_id):
        try:
            return self.sesion_ejercicio_repository.get_by_id(sesion_ejercicio_id)
        except Exception as e:
            print(f"Error en get_by_id del servicio de SesionEjercicio: {e}")
            return None

    def list(self):
        try:
            return self.sesion_ejercicio_repository.list()
        except Exception as e:
            print(f"Error en list del servicio de SesionEjercicio: {e}")
            return []

    def add(self, sesion_ejercicio):
        try:
            return self.sesion_ejercicio_repository.add(sesion_ejercicio)
        except Exception as e:
            print(f"Error en add del servicio de SesionEjercicio: {e}")
            return None

    def update(self, sesion_ejercicio):
        try:
            return self.sesion_ejercicio_repository.update(sesion_ejercicio)
        except Exception as e:
            print(f"Error en update del servicio de SesionEjercicio: {e}")
            return None

    def delete(self, sesion_ejercicio_id):
        try:
            return self.sesion_ejercicio_repository.delete(sesion_ejercicio_id)
        except Exception as e:
            print(f"Error en delete del servicio de SesionEjercicio: {e}")
            return None
