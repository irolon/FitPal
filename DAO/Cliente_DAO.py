from DAO.Base_DAO import BaseDAO
from Model.Cliente import Cliente

class ClienteDAO(BaseDAO):
    
    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cliente(
              usuario_id   INTEGER PRIMARY KEY,
              dni          TEXT NOT NULL,
              edad         INTEGER NOT NULL,
              fecha_inicio TEXT NOT NULL,
              FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()
        
    def create(self, id_usuario: int, c: Cliente) -> int:
        with self.conn:
            try:
                self.cur.execute(
                    "INSERT INTO cliente(usuario_id, dni, edad, fecha_inicio) VALUES (?,?,?,?) ON CONFLICT(usuario_id) DO NOTHING",
                    (id_usuario, c.dni, c.edad, c.fecha_inicio)
                )
                return self.cur.rowcount
            except Exception as e:
                print(f"Error al crear el cliente: {e}")
                return None
        
    def read_by_id(self, usuario_id:int):
        try:
            self.cur.execute("""SELECT usuario_id, dni, edad, fecha_inicio 
                            FROM cliente WHERE usuario_id = ?""", (usuario_id,))
            return self.cur.fetchone()
        except Exception as e:
            print(f"Error al leer el cliente por id: {e}")
            return None
    
    def delete(self, usuario_id: int) -> None:
        try:
            self.cur.execute("""DELETE FROM cliente WHERE usuario_id = ?""", (usuario_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el cliente: {e}")

    
    def update(self, c: Cliente, usuario_id: int) -> int:
        try:
            self.cur.execute("""
                UPDATE cliente
                SET dni = ?, edad = ?, fecha_inicio = ?
                WHERE usuario_id = ?
            """, (c.dni, c.edad, c.fecha_inicio, usuario_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(f"Error al actualizar el cliente: {e}")
            return None
    
    def list(self): 
        try:
            self.cur.execute(("""SELECT * FROM cliente"""))
            return self.cur.fetchall()
        except Exception as e:
            print(f"Error al leer todos los clientes: {e}")
            return None
