from DAO.Base_DAO import BaseDAO
from Model.Logros import Logros

class LogrosDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS logros(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  tipo          TEXT NOT NULL,
                  descripcion     TEXT,
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla logros: {e}")

    def create(self, l: Logros) -> int:
        try:
            self.cur.execute(
                """INSERT INTO logros(nombre, descripcion, puntos) 
                   VALUES (?,?,?)""",
                (l.nombre, l.descripcion, l.puntos)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear el logro: {e}")
            return None
    
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, nombre, descripcion, puntos 
                            FROM logros WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return Logros(
                nombre=row[1],
                descripcion=row[2],
                puntos=row[3],
                id=row[0]
            )
        except Exception as e:
            print(f"Error al leer el logro por id: {e}")
            return None
        
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM logros WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el logro: {e}")
            
    def update(self, l: Logros, id_: int) -> None:
        try:
            self.cur.execute(
                """UPDATE logros SET nombre = ?, descripcion = ?, puntos = ? WHERE id = ?""",
                (l.nombre, l.descripcion, l.puntos, id_)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar el logro: {e}")
            
    def list(self): 
        try:
            self.cur.execute(("""SELECT * FROM logros"""))
            rows = self.cur.fetchall()
            logros_list = []
            for row in rows:
                logro = Logros(
                    nombre=row[1],
                    descripcion=row[2],
                    puntos=row[3],
                    id=row[0]
                )
                logros_list.append(logro)
            return logros_list
        except Exception as e:
            print(f"Error al listar los logros: {e}")
            return None