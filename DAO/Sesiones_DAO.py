from DAO.Base_DAO import BaseDAO
from Model.Sesion import Sesion

class SesionesDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS sesion(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre          TEXT NOT NULL,
                  descripcion     TEXT NOT NULL,
                  estado          BOOLEAN NOT NULL DEFAULT 0
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla sesion: {e}")

    def create(self, s: Sesion) -> int:
        try:
            self.cur.execute(
                """INSERT INTO sesion(nombre, descripcion, estado) 
                   VALUES (?,?,?)""",
                (s.nombre, s.descripcion, s.estado)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear la sesión: {e}")
            return None
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, nombre, descripcion, estado 
                            FROM sesion WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            ses = Sesion(
                nombre=row[1],
                descripcion=row[2],
                id=row[0]
            )
            ses.estado = row[3]
            return ses
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
                """UPDATE sesion SET nombre = ?, descripcion = ?, estado = ? WHERE id = ?""",
                (s.nombre, s.descripcion, s.estado, id_)
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
                sesion = Sesion(
                    nombre=row[1],
                    descripcion=row[2],
                    id=row[0]
                )
                sesion.estado = row[3]
                sesiones.append(sesion)
            return sesiones
        except Exception as e:
            print(f"Error al listar las sesiones: {e}")
            return []
        
    def obtener_por_cliente_id(self, cliente_id: int):
        try:
            self.cur.execute("""
                SELECT DISTINCT s.id, s.nombre, s.descripcion, s.estado
                FROM sesion s
                JOIN plan_sesion ps ON s.id = ps.sesion_id
                JOIN plan_entrenamiento pe ON ps.plan_entrenamiento_id = pe.id
                WHERE pe.cliente_id = ?
                ORDER BY ps.orden
            """, (cliente_id,))
            rows = self.cur.fetchall()
            sesiones = []
            for row in rows:
                sesion = Sesion(
                    nombre=row[1],
                    descripcion=row[2],
                    id=row[0]
                )
                sesion.estado = row[3]
                sesiones.append(sesion)
            return sesiones
        except Exception as e:
            print(f"Error al obtener las sesiones por cliente_id: {e}")
            return []
    
    def actualizar_estado(self, sesion_id: int, estado: bool) -> bool:
        try:
            self.cur.execute(
                """UPDATE sesion SET estado = ? WHERE id = ?""",
                (estado, sesion_id)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar estado de la sesión: {e}")
            return False
        