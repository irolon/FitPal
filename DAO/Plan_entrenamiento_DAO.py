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
                administrador_id=row[1],
                cliente_id=row[2],
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
            # JOIN con la tabla usuario para obtener nombre y apellido del cliente
            self.cur.execute(("""
                SELECT p.id, p.administrador_id, p.cliente_id, p.nombre, p.frecuencia, 
                       p.fecha_inicio, p.fecha_fin, u.nombre as cliente_nombre, u.apellido as cliente_apellido
                FROM plan_entrenamiento p 
                LEFT JOIN usuario u ON p.cliente_id = u.id
            """))
            rows = self.cur.fetchall()
            planes = []
            for row in rows:
                plan = PlanEntrenamiento(
                    administrador_id=row[1],
                    cliente_id=row[2],
                    nombre=row[3],
                    frecuencia=row[4],
                    fecha_inicio=row[5],
                    fecha_fin=row[6],
                    id=row[0]
                )
                # Agregar nombre y apellido del cliente como atributos adicionales
                plan.cliente_nombre = row[7] if row[7] else ""
                plan.cliente_apellido = row[8] if row[8] else ""
                # Crear nombre completo o usar ID como fallback
                if plan.cliente_nombre or plan.cliente_apellido:
                    plan.cliente_nombre_completo = f"{plan.cliente_nombre} {plan.cliente_apellido}".strip()
                else:
                    plan.cliente_nombre_completo = f"ID: {row[2]}"
                planes.append(plan)
            return planes
        except Exception as e:
            print(f"Error al leer todos los planes de entrenamiento: {e}")
            return None
    
    def read_by_cliente_id(self, cliente_id: int):
        try:
            self.cur.execute("""SELECT id, administrador_id, cliente_id, nombre, frecuencia, fecha_inicio, fecha_fin 
                            FROM plan_entrenamiento WHERE cliente_id = ?""", (cliente_id,))
            rows = self.cur.fetchall()
            planes = []
            for row in rows:
                plan = PlanEntrenamiento(
                    administrador_id=row[1],
                    cliente_id=row[2],
                    nombre=row[3],
                    frecuencia=row[4],
                    fecha_inicio=row[5],
                    fecha_fin=row[6],
                    id=row[0]
                )
                planes.append(plan)
            return planes
        except Exception as e:
            print(f"Error al leer los planes de entrenamiento por cliente_id: {e}")
            return None