from DAO.Base_DAO import BaseDAO
from Model.Ejercicio import Ejercicio
from typing import List, Optional

class EjercicioDAO(BaseDAO):
    
    def create_table(self):
        try:
            self.cur.execute("""
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
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla ejercicios: {e}")
    
    def create(self, e: Ejercicio) -> Optional[int]:
        try:
            self.cur.execute("""
                INSERT INTO ejercicios (categoria, nombre, descripcion, repeticiones, series, descanso)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (e.categoria, e.nombre, e.descripcion, e.repeticiones, e.series, e.descanso))
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as ex:
            print(f"Error al crear el ejercicio: {ex}")
            return None
    
    def read_by_id(self, id_: int) -> Optional[Ejercicio]:
        try:
            self.cur.execute("""
                SELECT id, categoria, nombre, descripcion, repeticiones, series, descanso
                FROM ejercicios WHERE id = ?
            """, (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return Ejercicio(
                categoria=row[1],
                nombre=row[2],
                descripcion=row[3],
                repeticiones=row[4],
                series=row[5],
                descanso=row[6],
                id=row[0]
            )
        except Exception as ex:
            print(f"Error al leer ejercicio por id: {ex}")
            return None

    def update(self, e: Ejercicio, id_: int) -> Optional[int]:
        try:
            self.cur.execute("""
                UPDATE ejercicios
                SET categoria = ?, nombre = ?, descripcion = ?, repeticiones = ?, series = ?, descanso = ?
                WHERE id = ?
            """, (e.categoria, e.nombre, e.descripcion, e.repeticiones, e.series, e.descanso, id_))
            self.conn.commit()
        except Exception as ex:
            print(f"Error al actualizar ejercicio: {ex}")
            return None
    
    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("DELETE FROM ejercicios WHERE id = ?", (id_,))
            self.conn.commit()
        except Exception as ex:
            print(f"Error al eliminar ejercicio: {ex}")
    
    def list(self) -> List[Ejercicio]:
        try:
            self.cur.execute("""
                SELECT id, categoria, nombre, descripcion, repeticiones, series, descanso
                FROM ejercicios
            """)
            rows = self.cur.fetchall()
            ejercicios = []
            for row in rows:
                ejercicios.append(Ejercicio(
                    categoria=row[1],
                    nombre=row[2],
                    descripcion=row[3],
                    repeticiones=row[4],
                    series=row[5],
                    descanso=row[6],
                    id=row[0]
                ))
            return ejercicios
        except Exception as ex:
            print(f"Error al listar ejercicios: {ex}")
            return []
    
    def obtener_todos(self) -> List[Ejercicio]:
        return self.list()
    
    def obtener_por_id(self, id_: int) -> Optional[Ejercicio]:
        return self.read_by_id(id_)
    
    def insertar(self, e: Ejercicio) -> Optional[int]:
        return self.create(e)
    
    def actualizar(self, e: Ejercicio) -> bool:
        try:
            self.update(e, e.id)
            return True
        except Exception as ex:
            print(f"Error al actualizar ejercicio: {ex}")
            return False
    
    def eliminar(self, id_: int) -> bool:
        try:
            self.delete(id_)
            return True
        except Exception as ex:
            print(f"Error al eliminar ejercicio: {ex}")
            return False
