from DAO.Base_DAO import BaseDAO
import traceback

class ProgresoSesionDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS progreso_sesion(
                  id               INTEGER PRIMARY KEY AUTOINCREMENT,
                  cliente_id       INTEGER NOT NULL,
                  sesion_id        INTEGER NOT NULL,
                  estado           BOOLEAN NOT NULL DEFAULT 0,
                  fecha_completado DATE NULL,
                  UNIQUE(cliente_id, sesion_id),
                  FOREIGN KEY (cliente_id) REFERENCES cliente(usuario_id) ON DELETE CASCADE,
                  FOREIGN KEY (sesion_id) REFERENCES sesion(id) ON DELETE CASCADE
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla progreso_sesion: {e}")

    def obtener_progreso_por_cliente(self, cliente_id: int):
        try:
            self.cur.execute("""
                SELECT ps.sesion_id, ps.estado, ps.fecha_completado
                FROM progreso_sesion ps
                WHERE ps.cliente_id = ?
            """, (cliente_id,))
            rows = self.cur.fetchall()
            progreso = {}
            for row in rows:
                progreso[row[0]] = { 
                    'estado': row[1],
                    'fecha_completado': row[2]
                }
            return progreso
        except Exception as e:
            print(f"Error al obtener progreso por cliente: {e}")
            return {}

    def actualizar_o_crear_progreso(self, cliente_id: int, sesion_id: int, estado: bool):
        try:
            
            # Verificar si ya existe
            self.cur.execute("""
                SELECT id FROM progreso_sesion 
                WHERE cliente_id = ? AND sesion_id = ?
            """, (cliente_id, sesion_id))
            
            existe = self.cur.fetchone()
            
            if existe:
                # Actualizar existente
                self.cur.execute("""
                    UPDATE progreso_sesion 
                    SET estado = ?, 
                        fecha_completado = CASE 
                            WHEN ? = 1 THEN datetime('now')
                            ELSE NULL 
                        END
                    WHERE cliente_id = ? AND sesion_id = ?
                """, (estado, estado, cliente_id, sesion_id))
            else:
                # Crear nuevo
                print("Creando nuevo registro...")
                self.cur.execute("""
                    INSERT INTO progreso_sesion (cliente_id, sesion_id, estado, fecha_completado)
                    VALUES (?, ?, ?, CASE WHEN ? = 1 THEN datetime('now') ELSE NULL END)
                """, (cliente_id, sesion_id, estado, estado))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"ERROR en DAO actualizar_progreso: {e}")

            traceback.print_exc()
            return False

    def obtener_sesiones_con_progreso_por_cliente(self, cliente_id: int):
        try:
            self.cur.execute("""
                SELECT DISTINCT s.id, s.nombre, s.descripcion, 
                       COALESCE(ps.estado, 0) as estado,
                       ps.fecha_completado
                FROM sesion s
                JOIN plan_sesion pse ON s.id = pse.sesion_id
                JOIN plan_entrenamiento pe ON pse.plan_entrenamiento_id = pe.id
                LEFT JOIN progreso_sesion ps ON s.id = ps.sesion_id AND ps.cliente_id = ?
                WHERE pe.cliente_id = ?
                ORDER BY pse.orden
            """, (cliente_id, cliente_id))
            rows = self.cur.fetchall()
            sesiones = []
            for row in rows:
                sesion_data = {
                    'id': row[0],
                    'nombre': row[1],
                    'descripcion': row[2],
                    'estado': bool(row[3]),
                    'fecha_completado': row[4]
                }
                sesiones.append(sesion_data)
            return sesiones
        except Exception as e:
            print(f"Error al obtener sesiones con progreso: {e}")
            return []

    def create(self, progreso_data):
        pass
    
    def read_by_id(self, id_):
        try:
            self.cur.execute("SELECT * FROM progreso_sesion WHERE id = ?", (id_,))
            return self.cur.fetchone()
        except Exception as e:
            print(f"Error al leer progreso por id: {e}")
            return None
    
    def update(self, progreso_data, id_):
        pass
    
    def delete(self, id_):
        try:
            self.cur.execute("DELETE FROM progreso_sesion WHERE id = ?", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar progreso: {e}")
    
    def list(self):
        try:
            self.cur.execute("SELECT * FROM progreso_sesion")
            return self.cur.fetchall()
        except Exception as e:
            print(f"Error al listar progresos: {e}")
            return []