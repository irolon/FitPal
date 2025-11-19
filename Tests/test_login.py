import unittest
import json
from unittest.mock import MagicMock, patch
import sys
import os

# Configurar path para importaciones
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from app import app
from Model.Usuario import Usuario


class TestLogin(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        # Usuario registrado para los tests
        self.usuario_registrado = Usuario(
            id=1,
            nombre="Juan",
            apellido="Pérez",
            correo="juan@example.com",
            contrasena="password123",
            rol="cliente"
        )

    @patch('sqlite3.connect')
    @patch('routes.login_routes.UsuarioRepository')
    def test_usuario_registrado_existe(self, mock_repo_class, mock_connect):
        
        # Configurar mocks
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        mock_repo = MagicMock()
        mock_repo.list.return_value = [self.usuario_registrado]
        mock_repo_class.return_value = mock_repo
        
        # Hacer petición para verificar si el usuario existe
        response = self.client.post('/api/login', json={
            "username": "juan@example.com",
            "password": "password123"
        })
        
        # Verificar que el usuario está registrado (status != 404)
        self.assertNotEqual(response.status_code, 404, 
                           "El usuario debería estar registrado en el sistema")
        
        # Verificar que se encontraron usuarios
        mock_repo.list.assert_called_once()
        print("TEST USUARIO EXISTE: Usuario está registrado en el sistema")

    @patch('sqlite3.connect')
    @patch('routes.login_routes.UsuarioRepository')
    def test_login_con_credenciales_correctas(self, mock_repo_class, mock_connect):

        # Configurar mocks
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        mock_repo = MagicMock()
        mock_repo.list.return_value = [self.usuario_registrado]
        mock_repo_class.return_value = mock_repo
        
        # Intentar login con credenciales correctas
        response = self.client.post('/api/login', json={
            "username": "juan@example.com",
            "password": "password123"
        })
        
        # Verificar login exitoso
        self.assertEqual(response.status_code, 200, 
                        "El login debería ser exitoso con credenciales correctas")
        
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Login successful')
        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['nombre'], "Juan")
        self.assertEqual(data['apellido'], "Pérez")
        self.assertEqual(data['rol'], "cliente")
        
        print("TEST USUARIO CORRECTO: Login exitoso con credenciales correctas")

    @patch('sqlite3.connect')
    @patch('routes.login_routes.UsuarioRepository')
    def test_login_con_credenciales_incorrectas(self, mock_repo_class, mock_connect):
        
        # Configurar mocks
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        mock_repo = MagicMock()
        mock_repo.list.return_value = [self.usuario_registrado]
        mock_repo_class.return_value = mock_repo
        
        # Intentar login con contraseña incorrecta
        response = self.client.post('/api/login', json={
            "username": "juan@example.com",
            "password": "password_INCORRECTO"
        })
        
        # Verificar que el login fue rechazado
        self.assertEqual(response.status_code, 401, 
                        "El login debería fallar con credenciales incorrectas")
        
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Invalid credentials')
    
        print("TEST USUARIO INCORRECTO: Login fallido con credenciales incorrectas")

    @patch('sqlite3.connect')
    @patch('routes.login_routes.UsuarioRepository')
    def test_login_usuario_no_registrado(self, mock_repo_class, mock_connect):
                
        # Configurar mocks
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        mock_repo = MagicMock()
        mock_repo.list.return_value = []  # Base de datos vacía
        mock_repo_class.return_value = mock_repo
        
        # Intentar login con usuario no registrado
        response = self.client.post('/api/login', json={
            "username": "usuario@noexiste.com",
            "password": "cualquier_password"
        })
        
        # Verificar que no se encontraron usuarios
        self.assertEqual(response.status_code, 404, 
                        "Debería retornar 404 cuando no hay usuarios registrados")
        
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'No users found')
        
        print("TEST USUARIO NO REGISTRADO: Usuario no registrado correctamente detectado")

    def tearDown(self):
        """Limpieza después de cada test"""
        pass


def suite():
    """Crear suite de tests"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestLogin('test_usuario_registrado_existe'))
    test_suite.addTest(TestLogin('test_login_con_credenciales_correctas'))
    test_suite.addTest(TestLogin('test_login_con_credenciales_incorrectas'))
    test_suite.addTest(TestLogin('test_login_usuario_no_registrado'))
    return test_suite


if __name__ == '__main__':
    print("TESTS DE LOGIN")

    print("\n - Verificar que el usuario esté registrado")
    print(" - Login con credenciales correctas")
    print(" - Login con credenciales incorrectas")
    print(" - Usuario no registrado (test adicional)")
    print("-" * 50)
    
    # Cambiar al directorio padre para ejecutar
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir)
    
    # Ejecutar tests con unittest
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    

    print("\n RESUMEN DE RESULTADOS:")
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Errores: {len(result.errors)}")
    print(f"Fallos: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("\nTEST COMPLETADOS CORRECTAMENTE")
    else:
        print("\nALGUNOS TESTS FALLARON")
        if result.errors:
            print("\nErrores:")
            for test, error in result.errors:
                print(f"  - {test}: {error}")
        if result.failures:
            print("\nFallos:")
            for test, failure in result.failures:
                print(f"  - {test}: {failure}")
    
