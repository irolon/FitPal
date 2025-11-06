from Model.Usuario import Usuario
from DAO.Usuario_DAO import UsuarioDAO
import pytest

def test_create_inserta_y_devuelve_id(usuario_dao):
    u = Usuario(nombre="Ana", apellido="García", correo="ana@test.com", contrasena="hash", rol="cliente")
    new_id = usuario_dao.create(u)
    assert isinstance(new_id, int)

def test_create_falla_por_correo_duplicado(usuario_dao):
    u1 = Usuario("Ana","G","ana@test.com","h","cliente")
    u2 = Usuario("Juan","P","ana@test.com","h","cliente")
    usuario_dao.create(u1)
    with pytest.raises(Exception):            # o sqlite3.IntegrityError si lo propagás
        usuario_dao.create(u2)

def test_list_devuelve_modelos(usuario_dao):
    usuario_dao.create(Usuario("A","A","a@test.com","h","cliente"))
    usuario_dao.create(Usuario("B","B","b@test.com","h","administrador"))
    lista = usuario_dao.list_all()
    assert len(lista) == 2
    assert all(hasattr(x, "correo") for x in lista)