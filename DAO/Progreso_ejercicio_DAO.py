from DAO.Base_DAO import BaseDAO
from typing import List, Optional
import traceback

class ProgresoEjercicioDAO(BaseDAO):
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS progreso_ejercicio(
                  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
                  cliente_id        INTEGER NOT NULL,
                  ejercicio_id      INTEGER NOT NULL,
                  estado            TEXT NOT NULL DEFAULT 'pendiente',
                  fecha_completado  DATETIME,
                  fecha_creacion    DATETIME DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY (cliente_id) REFERENCES cliente(usuario_id) ON DELETE CASCADE,
                  FOREIGN KEY (ejercicio_id) REFERENCES ejercicios(id) ON DELETE CASCADE,
                  UNIQUE(cliente_id, ejercicio_id)
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla progreso_ejercicio: {e}")

    def obtener_progreso_por_cliente(self, cliente_id: int):
        """Obtiene el progreso de todos los ejercicios para un cliente"""
        try:
            self.cur.execute("""
                SELECT ejercicio_id, estado, fecha_completado
                FROM progreso_ejercicio
                WHERE cliente_id = ?
            """, (cliente_id,))
            rows = self.cur.fetchall()
            
            # Convertir a diccionario para fácil acceso
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

    def actualizar_estado_ejercicio(self, cliente_id: int, ejercicio_id: int, nuevo_estado: str):
        """Actualiza el estado de un ejercicio específico para un cliente"""
        try:
            from datetime import datetime
            fecha_completado = datetime.now().isoformat() if nuevo_estado == 'completado' else None
            
            
            self.cur.execute(
                """INSERT OR REPLACE INTO progreso_ejercicio(cliente_id, ejercicio_id, estado, fecha_completado) 
                   VALUES (?,?,?,?)""",
                (cliente_id, ejercicio_id, nuevo_estado, fecha_completado)
            )
            self.conn.commit()
            
            return True
        except Exception as e:
            print(f"❌ DAO Error al actualizar estado ejercicio: {e}")
            traceback.print_exc()
            self.conn.rollback()
            return False

    # Métodos abstractos requeridos por BaseDAO
    def create(self, progreso_data):
        """Método requerido por BaseDAO"""
        try:
            return self.actualizar_estado_ejercicio(
                progreso_data.get('cliente_id'),
                progreso_data.get('ejercicio_id'),
                progreso_data.get('estado', 'pendiente')
            )
        except Exception as e:
            print(f"Error en create: {e}")
            return None
    
    def read_by_id(self, id_):
        """Método requerido por BaseDAO"""
        try:
            self.cur.execute("""
                SELECT id, cliente_id, ejercicio_id, estado, fecha_completado, fecha_creacion 
                FROM progreso_ejercicio WHERE id = ?
            """, (id_,))
            return self.cur.fetchone()
        except Exception as e:
            print(f"Error al leer progreso por id: {e}")
            return None
    
    def update(self, progreso_data, id_):
        """Método requerido por BaseDAO"""
        try:
            self.cur.execute("""
                UPDATE progreso_ejercicio 
                SET estado = ?, fecha_completado = ?
                WHERE id = ?
            """, (progreso_data.get('estado'), progreso_data.get('fecha_completado'), id_))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar progreso: {e}")
            return False
    
    def delete(self, id_):
        """Método requerido por BaseDAO"""
        try:
            self.cur.execute("DELETE FROM progreso_ejercicio WHERE id = ?", (id_,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar progreso: {e}")
            self.conn.rollback()
            return False
    
    def list(self):
        """Método requerido por BaseDAO"""
        try:
            self.cur.execute("""
                SELECT id, cliente_id, ejercicio_id, estado, fecha_completado, fecha_creacion 
                FROM progreso_ejercicio
            """)
            rows = self.cur.fetchall()
            progresos = []
            for row in rows:
                progresos.append({
                    'id': row[0],
                    'cliente_id': row[1],
                    'ejercicio_id': row[2],
                    'estado': row[3],
                    'fecha_completado': row[4],
                    'fecha_creacion': row[5]
                })
            return progresos
        except Exception as e:
            print(f"Error al listar los progresos: {e}")
            return []