from DAO.Base_DAO import BaseDAO
from Model.Ejercicio import Ejercicio
import sqlite3

class Ejercicio_DAO:
    def __init__(self, db_path: str = "fitpal.db"):
        self.db_path = db_path
        self._crear_tabla()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _crear_tabla(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ejercicios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria TEXT NOT NULL,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                repeticiones INTEGER,
                series INTEGER,
                descanso INTEGER
            )
        """)
        conn.commit()
        conn.close()

    def insertar(self, ejercicio: Ejercicio) -> int:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ejercicios (categoria, nombre, descripcion, repeticiones, series, descanso)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (ejercicio.categoria, ejercicio.nombre, ejercicio.descripcion,
              ejercicio.repeticiones, ejercicio.series, ejercicio.descanso))
        conn.commit()
        ejercicio_id = cursor.lastrowid
        conn.close()
        return ejercicio_id

    def obtener_todos(self) -> list[Ejercicio]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, categoria, nombre, descripcion, repeticiones, series, descanso FROM ejercicios")
        filas = cursor.fetchall()
        conn.close()
        return [Ejercicio(id=f[0], categoria=f[1], nombre=f[2], descripcion=f[3],
                          repeticiones=f[4], series=f[5], descanso=f[6]) for f in filas]

    def obtener_por_id(self, id: int) -> Ejercicio | None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, categoria, nombre, descripcion, repeticiones, series, descanso FROM ejercicios WHERE id = ?", (id,))
        fila = cursor.fetchone()
        conn.close()
        if fila:
            return Ejercicio(id=fila[0], categoria=fila[1], nombre=fila[2], descripcion=fila[3],
                             repeticiones=fila[4], series=fila[5], descanso=fila[6])
        return None

    def actualizar(self, ejercicio: Ejercicio) -> bool:
        if ejercicio.id is None:
            return False
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE ejercicios
            SET categoria = ?, nombre = ?, descripcion = ?, repeticiones = ?, series = ?, descanso = ?
            WHERE id = ?
        """, (ejercicio.categoria, ejercicio.nombre, ejercicio.descripcion,
              ejercicio.repeticiones, ejercicio.series, ejercicio.descanso, ejercicio.id))
        conn.commit()
        actualizado = cursor.rowcount > 0
        conn.close()
        return actualizado

    def eliminar(self, id: int) -> bool:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ejercicios WHERE id = ?", (id,))
        conn.commit()
        eliminado = cursor.rowcount > 0
        conn.close()
        return eliminado
