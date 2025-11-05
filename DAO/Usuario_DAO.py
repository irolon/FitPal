from DAO.Base_DAO import BaseDAO
from Model.Usuario import Usuario

class UsuarioDAO(BaseDAO):
    
    def create_table(self):
        try:
            
            self.cur.execute(('''        CREATE TABLE IF NOT EXISTS usuario (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre     TEXT NOT NULL,
                apellido   TEXT NOT NULL,
                correo     TEXT NOT NULL UNIQUE,
                contrasena TEXT NOT NULL,
                rol        TEXT NOT NULL CHECK(rol IN ('administrador','cliente'))
            )'''))
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear la tabla usuario: {e}")

        
    def create(self, u: Usuario) -> int:
        try:
            self.cur.execute(
                """INSERT INTO usuario(nombre, apellido, correo, contrasena, rol) VALUES (?,?,?,?,?)""",
                (u.nombre, u.apellido, u.correo, u.contrasena, u.rol)
            )
            self.conn.commit()
            return self.cur.lastrowid
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return None
        
    def read_by_id(self, id_: int) -> Usuario | None:
        try:
            self.cur.execute("""SELECT id, nombre, apellido, 
                            correo, contrasena, rol
                            FROM usuario WHERE id = ? """, (id_,))
            row = self.cur.fetchone()
            if not row:
                return None
            return Usuario(
                nombre=row[1],
                apellido=row[2],
                correo=row[3],
                contrasena=row[4],
                rol=row[5],
                id=row[0],
            )
        except Exception as e:
            print(f"Error al leer el usuario por id: {e}")
            return None

    def delete(self, id_: int) -> None:
        try:
            self.cur.execute("""DELETE FROM usuario WHERE id = ?""", (id_,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")

    def update(self, u: Usuario, id_: int) -> int:
        try:
            self.cur.execute("""
                UPDATE usuario
                SET nombre = ?, apellido = ?, correo = ?, contrasena = ?, rol = ?
                WHERE id = ?
            """, (u.nombre, u.apellido, u.correo, u.contrasena, u.rol, id_))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(f"Error al actualizar el usuario: {e}")
            return None

    def list(self): 
        try:
            self.cur.execute(("""SELECT * FROM usuario"""))
            return self.cur.fetchall()
        except Exception as e:
            print(f"Error al leer todos los usuarios: {e}")
            return None
    
    def read_by_email(self, correo: str) -> Usuario | None:
        try:
            self.cur.execute("""SELECT id, nombre, apellido, 
                            correo, contrasena, rol
                            FROM usuario WHERE correo = ? """, (correo,))
            row = self.cur.fetchone()
            if not row:
                return None
            return Usuario(
                nombre=row[1],
                apellido=row[2],
                correo=row[3],
                contrasena=row[4],
                rol=row[5],
                id=row[0],
            )
        except Exception as e:
            print(f"Error al leer el usuario por correo: {e}")
            return None