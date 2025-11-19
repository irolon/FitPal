from DAO.Base_DAO import BaseDAO
from Model.Sesion_ejercicio import SesionEjercicio

class SesionEjercicioDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS sesion_ejercicio(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  sesion_id       INTEGER NOT NULL,
                  ejercicio_id    INTEGER NOT NULL,
                  series          INTEGER NOT NULL,
                  repeticiones    INTEGER NOT NULL,
                  descanso        INTEGER NOT NULL,
                  FOREIGN KEY (sesion_id) REFERENCES sesion(id) ON DELETE CASCADE,
                  FOREIGN KEY (ejercicio_id) REFERENCES ejercicios(id) ON DELETE CASCADE
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla sesion_ejercicio: {e}")

    def create(self, s: SesionEjercicio) -> int:
        try:
            self.cur.execute(
                """INSERT INTO sesion_ejercicio(sesion_id, ejercicio_id, series, repeticiones, descanso) 
                   VALUES (?,?,?,?,?)""",
                (s.sesion_id, s.ejercicio_id, s.series, s.repeticiones, s.descanso)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear la sesión ejercicio: {e}")
            return None
    
    def read_by_id(self, id_:int):
        try:
            self.cur.execute("""SELECT id, sesion_id, ejercicio_id, series, repeticiones, descanso 
                            FROM sesion_ejercicio WHERE id = ?""", (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return SesionEjercicio(
                sesion_id=row[1],
                ejercicio_id=row[2],
                series=row[3],
                repeticiones=row[4],
                descanso=row[5],
                id=row[0]
            )
        except Exception as e:
            print(f"Error al leer la sesión ejercicio por id: {e}")
            return None
        
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM sesion_ejercicio WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar la sesión ejercicio: {e}")
            
    def update(self, s: SesionEjercicio, id_: int) -> None:
        try:
            self.cur.execute(
                """UPDATE sesion_ejercicio 
                   SET sesion_id = ?, ejercicio_id = ?, series = ?, repeticiones = ?, descanso = ? 
                   WHERE id = ?""",
                (s.sesion_id, s.ejercicio_id, s.series, s.repeticiones, s.descanso, id_)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar la sesión ejercicio: {e}")
            
    def list(self):
        try:
            self.cur.execute(("""SELECT id, sesion_id, ejercicio_id, series, repeticiones, descanso FROM sesion_ejercicio"""))
            rows = self.cur.fetchall()
            sesiones_ejercicios = []
            for row in rows:
                sesiones_ejercicios.append(
                    SesionEjercicio(
                        sesion_id=row[1],
                        ejercicio_id=row[2],
                        series=row[3],
                        repeticiones=row[4],
                        descanso=row[5],
                        id=row[0]
                    )
                )
            return sesiones_ejercicios
        except Exception as e:
            print(f"Error al listar las sesiones ejercicios: {e}")
            return None

    def obtener_por_sesion(self, sesion_id: int):
        try:
            # Hacer JOIN para obtener información completa de los ejercicios
            self.cur.execute("""
                SELECT se.id, se.sesion_id, se.ejercicio_id, se.series, se.repeticiones, se.descanso,
                       e.nombre, e.descripcion, e.categoria
                FROM sesion_ejercicio se
                JOIN ejercicios e ON se.ejercicio_id = e.id
                WHERE se.sesion_id = ?
                ORDER BY se.id
            """, (sesion_id,))
            rows = self.cur.fetchall()
            ejercicios = []
            for row in rows:
                # Devolver un diccionario con toda la información del ejercicio
                ejercicios.append({
                    'id': row[2],  # ejercicio_id
                    'nombre': row[6],
                    'descripcion': row[7], 
                    'categoria': row[8],
                    'series': row[3],
                    'repeticiones': row[4],
                    'descanso': row[5],
                    'sesion_ejercicio_id': row[0]  # id de la fk
                })
            return ejercicios
        except Exception as e:
            print(f"Error al obtener ejercicios por sesión: {e}")
            return []

    def delete_by_sesion(self, sesion_id: int):
        try:
            self.cur.execute("DELETE FROM sesion_ejercicio WHERE sesion_id = ?", (sesion_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar ejercicios de la sesión: {e}")
        

    def get_ejercicios_por_cliente(self, cliente_id: int):
        try:
            self.cur.execute("""
                SELECT DISTINCT e.id, e.categoria, e.nombre, e.descripcion, e.repeticiones, e.series, e.descanso
                FROM ejercicios e
                JOIN sesion_ejercicio se ON e.id = se.ejercicio_id
                JOIN sesion s ON se.sesion_id = s.id
                JOIN plan_sesion ps ON s.id = ps.sesion_id
                JOIN plan_entrenamiento pe ON ps.plan_entrenamiento_id = pe.id
                WHERE pe.cliente_id = ?
                ORDER BY e.categoria, e.nombre
            """, (cliente_id,))
            rows = self.cur.fetchall()
            ejercicios = []
            for row in rows:
                ejercicios.append({
                    'id': row[0],
                    'categoria': row[1],
                    'nombre': row[2],
                    'descripcion': row[3],
                    'repeticiones': row[4],
                    'series': row[5],
                    'descanso': row[6]
                })
            return ejercicios
        except Exception as e:
            print(f"Error al obtener ejercicios por cliente: {e}")
            return []

    def crear_relacion_simple(self, sesion_id: int, ejercicio_id: int) -> int:
        try:
            # Usar valores por defecto para series, repeticiones, descanso
            self.cur.execute(
                """INSERT INTO sesion_ejercicio(sesion_id, ejercicio_id, series, repeticiones, descanso) 
                   VALUES (?,?,3,12,60)""", 
                (sesion_id, ejercicio_id)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear la relación sesión-ejercicio: {e}")
            return None

    def agregar_ejercicio(self, sesion_id: int, ejercicio_id: int):
        return self.crear_relacion_simple(sesion_id, ejercicio_id)

    def eliminar_ejercicio(self, sesion_id: int, ejercicio_id: int):
        try:
            self.cur.execute(
                "DELETE FROM sesion_ejercicio WHERE sesion_id = ? AND ejercicio_id = ?",
                (sesion_id, ejercicio_id)
            )
            self.conn.commit()
            return "Ejercicio eliminado de la sesión con éxito"
        except Exception as e:
            print(f"Error al eliminar ejercicio de la sesión: {e}")
            return None