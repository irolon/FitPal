from DAO.Base_DAO import BaseDAO
from Model.Plan_Sesion import PlanSesion

class PlanSesionDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS plan_sesion(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  plan_entrenamiento_id INTEGER NOT NULL,
                  sesion_id       INTEGER NOT NULL,
                  orden          INTEGER NOT NULL,
                  FOREIGN KEY (plan_entrenamiento_id) REFERENCES plan_entrenamiento(id) ON DELETE CASCADE,
                  FOREIGN KEY (sesion_id) REFERENCES sesion(id) ON DELETE CASCADE
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla plan_sesion: {e}")

    def create(self, plan_entrenamiento_id: int, sesion_id: int, orden: int = 1) -> int:
        try:
            self.cur.execute(
                """INSERT INTO plan_sesion(plan_entrenamiento_id, sesion_id, orden) 
                   VALUES (?,?,?)""",
                (plan_entrenamiento_id, sesion_id, orden)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear el plan de sesión: {e}")
            return None
        
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, plan_entrenamiento_id, sesion_id, orden 
                            FROM plan_sesion WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return PlanSesion(
                plan_id=row[1],
                sesion_id=row[2],
                orden=row[3],
                id=row[0]
            )
        except Exception as e:
            print(f"Error al leer el plan de sesión por id: {e}")
            return None
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM plan_sesion WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el plan de sesión: {e}")
    
    def update(self, p: PlanSesion, id_: int) -> None:
        try:
            self.cur.execute(
                """UPDATE plan_sesion 
                   SET plan_entrenamiento_id = ?, sesion_id = ?, orden = ? 
                   WHERE id = ?""",
                (p.plan_id, p.sesion_id, p.orden, id_)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar el plan de sesión: {e}")
            
    def list(self):
        try:
            self.cur.execute(("""SELECT id, plan_entrenamiento_id, sesion_id, orden FROM plan_sesion"""))
            rows = self.cur.fetchall()
            planes_sesiones = []
            for row in rows:
                planes_sesiones.append(
                    PlanSesion(
                        plan_id=row[1],
                        sesion_id=row[2],
                        orden=row[3],
                        id=row[0]
                    )
                )
            return planes_sesiones
        except Exception as e:
            print(f"Error al listar los planes de sesión: {e}")
            return None
    
    def read_by_cliente_id(self, cliente_id: int):
        try:
            self.cur.execute("""
                SELECT ps.id, ps.plan_entrenamiento_id, ps.sesion_id, ps.orden 
                FROM plan_sesion ps
                JOIN plan_entrenamiento pe ON ps.plan_entrenamiento_id = pe.id
                WHERE pe.cliente_id = ?
            """, (cliente_id,))
            rows = self.cur.fetchall()
            planes_sesiones = []
            for row in rows:
                planes_sesiones.append(
                    PlanSesion(
                        plan_id=row[1],
                        sesion_id=row[2],
                        orden=row[3],
                        id=row[0]
                    )
                )
            return planes_sesiones
        except Exception as e:
            print(f"Error al buscar planes de sesión por cliente_id: {e}")
            return []
        
    