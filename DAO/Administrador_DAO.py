from DAO.Base_DAO import BaseDAO
from Model.Administrador import Administrador

class AdministradorDAO(BaseDAO):
    
    def create_table(self):
        self.cur.execute(('''CREATE TABLE IF NOT EXISTS administrador(usuario_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             activo INTEGER NOT NULL CHECK(activo IN(0,1)), fecha_alta DATE NOT NULL,
                             FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE)'''))
        self.conn.commit()
        
    def create(self, id_usuario: int, a: Administrador) -> int:
        try:
            self.cur.execute(
                """INSERT INTO administrador(usuario_id, activo, fecha_alta) VALUES (?,?,?)  ON CONFLICT(usuario_id) DO NOTHING""",
                (id_usuario, a.activo, a.fecha_alta)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear el administrador: {e}")
            return None

    
    def read_by_id(self, usuario_id:int):
        try:
            self.cur.execute("""SELECT usuario_id, activo, fecha_alta 
                            FROM administrador WHERE usuario_id = ?""", (usuario_id,))
            return self.cur.fetchone()
        except Exception as e:
            print(f"Error al leer el administrador por id: {e}")
            return None
    
    def delete(self, usuario_id: int) -> None:
        try:
            self.cur.execute("""DELETE FROM administrador WHERE usuario_id = ?""", (usuario_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el administrador: {e}")

        
    def update(self, a: Administrador, usuario_id: int) -> int:
        try:
            self.cur.execute("""
                UPDATE administrador
                SET activo = ?, fecha_alta = ?
                WHERE usuario_id = ?
            """, (a.activo, a.fecha_alta, usuario_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(f"Error al actualizar el administrador: {e}")
            return None
            
    def list(self): 
        try:
            self.cur.execute(("""SELECT * FROM administrador"""))
            return self.cur.fetchall()
        except Exception as e:
            print(f"Error al leer todos los administradores: {e}")
            return None
