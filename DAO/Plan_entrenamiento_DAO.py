from DAO.Base_DAO import BaseDAO
from Model.Plan_entrenamiento import PlanEntrenamiento

class PlanEntrenamientoDAO(BaseDAO):
    
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS plan_entrenamiento(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  administrador_id   INTEGER NOT NULL,
                  cliente_id      INTEGER NOT NULL,
                  nombre          TEXT NOT NULL,
                  frecuencia      INTEGER NOT NULL,
                  fecha_inicio   DATE NOT NULL,
                  fecha_fin      DATE NOT NULL,
                  FOREIGN KEY (cliente_id) REFERENCES cliente(usuario_id) ON DELETE CASCADE
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla plan_entrenamiento: {e}")

    def create(self, administrador_id: int, cliente_id: int, p: PlanEntrenamiento) -> int:
        try:
            self.cur.execute(
                """INSERT INTO plan_entrenamiento(administrador_id, cliente_id, nombre, frecuencia, fecha_inicio, fecha_fin) 
                   VALUES (?,?,?,?,?,?)""",
                (administrador_id, cliente_id, p.nombre, p.frecuencia, p.fecha_inicio, p.fecha_fin)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear el plan de entrenamiento: {e}")
            return None
        
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, administrador_id, cliente_id, nombre, frecuencia, fecha_inicio, fecha_fin 
                            FROM plan_entrenamiento WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return PlanEntrenamiento(
                nombre=row[3],
                frecuencia=row[4],
                fecha_inicio=row[5],
                fecha_fin=row[6],
                id=row[0]
            )
        except Exception as e:
            print(f"Error al leer el plan de entrenamiento por id: {e}")
            return None
    
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM plan_entrenamiento WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el plan de entrenamiento: {e}")
            
    def update(self, p: PlanEntrenamiento, id_: int) -> int:
        try:
            self.cur.execute("""
                UPDATE plan_entrenamiento
                SET nombre = ?, frecuencia = ?, fecha_inicio = ?, fecha_fin = ?
                WHERE id = ?
            """, (p.nombre, p.frecuencia, p.fecha_inicio, p.fecha_fin, id_))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(f"Error al actualizar el plan de entrenamiento: {e}")
            return None
        
    def list(self): 
        try:
            self.cur.execute(("""SELECT * FROM plan_entrenamiento"""))
            rows = self.cur.fetchall()
            planes = []
            for row in rows:
                plan = PlanEntrenamiento(
                    nombre=row[3],
                    frecuencia=row[4],
                    fecha_inicio=row[5],
                    fecha_fin=row[6],
                    id=row[0]
                )
                planes.append(plan)
            return planes
        except Exception as e:
            print(f"Error al leer todos los planes de entrenamiento: {e}")
            return None