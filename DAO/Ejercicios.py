from DAO.Base_DAO import BaseDAO
from Model.Ejercicios import Ejercicios

class EjerciciosDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS ejercicios(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre          TEXT NOT NULL,
                  descripcion     TEXT,
                  duracion        INTEGER,
                  nivel_dificultad TEXT
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla ejercicios: {e}")

    def create(self, e: Ejercicios) -> int:
        try:
            self.cur.execute(
                """INSERT INTO ejercicios(nombre, descripcion, duracion, nivel_dificultad) 
                   VALUES (?,?,?,?)""",
                (e.nombre, e.descripcion, e.duracion, e.nivel_dificultad)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear el ejercicio: {e}")
            return None
        
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, nombre, descripcion, duracion, nivel_dificultad 
                            FROM ejercicios WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return Ejercicios(
                nombre=row[1],
                descripcion=row[2],
                duracion=row[3],
                nivel_dificultad=row[4],
                id=row[0]
            )
        except Exception as e:
            print(f"Error al leer el ejercicio por id: {e}")
            return None
        
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM ejercicios WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el ejercicio: {e}")
            
    def update(self, e: Ejercicios, id_: int) -> None:
        try:
            self.cur.execute(
                """UPDATE ejercicios 
                   SET nombre = ?, descripcion = ?, duracion = ?, nivel_dificultad = ? 
                   WHERE id = ?""",
                (e.nombre, e.descripcion, e.duracion, e.nivel_dificultad, id_)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar el ejercicio: {e}")
            
    def list(self):
        try:
            self.cur.execute(("""SELECT id, nombre, descripcion, duracion, nivel_dificultad FROM ejercicios"""))
            rows = self.cur.fetchall()
            ejercicios = []
            for row in rows:
                ejercicios.append(
                    Ejercicios(
                        nombre=row[1],
                        descripcion=row[2],
                        duracion=row[3],
                        nivel_dificultad=row[4],
                        id=row[0]
                    )
                )
            return ejercicios
        except Exception as e:
            print(f"Error al listar los ejercicios: {e}")
            return []