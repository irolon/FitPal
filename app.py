import sqlite3
from DAO.Administrador_DAO import AdministradorDAO
from DAO.Cliente_DAO import ClienteDAO
from DAO.Usuario_DAO import UsuarioDAO
from Model.Administrador import Administrador
from Model.Cliente import Cliente
from Model.Plan_entrenamiento import PlanEntrenamiento
from Model.Usuario import Usuario
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO
from Repository.Usuario_repository import UsuarioRepository

conn = sqlite3.connect('data_base/db_fitpal.db')

repoUsuario = UsuarioRepository(conn)
otro = Usuario("Juan", "Pérez", "juan@mail.com", "1234", "cliente")

id_creado = repoUsuario.add(otro)
print("ID creado:", id_creado)

