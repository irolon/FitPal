from DAO.Base_DAO import BaseDAO
from Model.Sesion import Sesion

class SesionesDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS sesion(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre          TEXT NOT NULL,
                  duracion        INTEGER NOT NULL,
                  descripcion     TEXT
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla sesion: {e}")

    def create(self, s: Sesion) -> int:
        try:
            self.cur.execute(
                """INSERT INTO sesion(nombre, duracion, descripcion) 
                   VALUES (?,?,?)""",
                (s.nombre, s.duracion, s.descripcion)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear la sesión: {e}")
            return None
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, nombre, duracion, descripcion 
                            FROM sesion WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return Sesion(
                nombre=row[1],
                duracion=row[2],
                descripcion=row[3],
                id=row[0]
            )
        except Exception as e:
            print(f"Error al leer la sesión por id: {e}")
            return None
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM sesion WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar la sesión: {e}")
            
    def update(self, s: Sesion, id_: int) -> None:
        try:
            self.cur.execute(
                """UPDATE sesion SET nombre = ?, duracion = ?, descripcion = ? WHERE id = ?""",
                (s.nombre, s.duracion, s.descripcion, id_)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar la sesión: {e}")
            
    def list(self): 
        try:
            self.cur.execute(("""SELECT * FROM sesion"""))
            rows = self.cur.fetchall()
            sesiones = []
            for row in rows:
                sesiones.append(Sesion(
                    nombre=row[1],
                    duracion=row[2],
                    descripcion=row[3],
                    id=row[0]
                ))
            return sesiones
        except Exception as e:
            print(f"Error al listar las sesiones: {e}")
            return []