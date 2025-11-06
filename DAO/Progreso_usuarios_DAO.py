from DAO.Base_DAO import BaseDAO
from Model.Progreso_usuario import ProgresoUsuario

class ProgresoUsuariosDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS progreso_usuarios(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  usuario_id      INTEGER NOT NULL,
                  logro_id       INTEGER NOT NULL,
                  fecha_cumplido           DATE NOT NULL,
                  puntaje_logro        INTEGER NOT NULL,
                  nivel         INTEGER NOT NULL,
                  FOREIGN KEY (usuario_id) REFERENCES cliente(usuario_id) ON DELETE CASCADE,
                  FOREIGN KEY (logro_id) REFERENCES logros(id) ON DELETE CASCADE
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla progreso_usuarios: {e}")

    def create(self, usuario_id: int, p: ProgresoUsuario) -> int:
        try:
            self.cur.execute(
                """INSERT INTO progreso_usuarios(usuario_id, fecha, peso, porcentaje_grasa) 
                   VALUES (?,?,?,?)""",
                (usuario_id, p.fecha, p.peso, p.porcentaje_grasa)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear el progreso del usuario: {e}")
            return None
        
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, usuario_id, fecha, peso, porcentaje_grasa 
                            FROM progreso_usuarios WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return ProgresoUsuario(
                fecha=row[2],
                peso=row[3],
                porcentaje_grasa=row[4],
                id=row[0]
            )
        except Exception as e:
            print(f"Error al leer el progreso del usuario por id: {e}")
            return None
        
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM progreso_usuarios WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el progreso del usuario: {e}")
            
    def update(self, p: ProgresoUsuario, id_: int) -> None:
        try:
            self.cur.execute(
                """UPDATE progreso_usuarios
                   SET fecha = ?, peso = ?, porcentaje_grasa = ?
                   WHERE id = ?""",
                (p.fecha, p.peso, p.porcentaje_grasa, id_)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar el progreso del usuario: {e}")
            
    def list(self):
        try:
            self.cur.execute(("""SELECT * FROM progreso_usuarios"""))
            rows = self.cur.fetchall()
            progresos = []
            for row in rows:
                progresos.append(
                    ProgresoUsuario(
                        fecha=row[2],
                        peso=row[3],
                        porcentaje_grasa=row[4],
                        id=row[0]
                    )
                )
            return progresos
        except Exception as e:
            print(f"Error al listar los progresos de usuarios: {e}")
            return None