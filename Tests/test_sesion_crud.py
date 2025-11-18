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
from Model.Sesion import Sesion


class TestSesionCRUD(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada test"""
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        # Sesion de ejemplo para los tests
        self.sesion_ejemplo = Sesion(
            id=1,
            nombre="Entrenamiento de Pecho",
            descripcion="Sesion completa para fortalecer musculos pectorales"
        )
        
        # Datos para crear una nueva sesion
        self.nueva_sesion_data = {
            "nombre": "Entrenamiento de Espalda",
            "descripcion": "Sesion completa para fortalecer musculos dorsales"
        }
        
        # Datos para actualizar una sesion
        self.sesion_actualizada_data = {
            "nombre": "Entrenamiento de Pecho Avanzado",
            "descripcion": "Sesion avanzada para pectoral superior e inferior"
        }

    def tearDown(self):
        """Limpieza despues de cada test"""
        pass

    @patch('routes.sesion_routes.service')
    def test_crear_sesion(self, mock_service):
        
        # Configurar mock del servicio
        mock_service.add.return_value = 2  
        
        # Enviar peticion POST para crear sesion
        response = self.client.post('/api/admin/sesiones',
                                   json=self.nueva_sesion_data,
                                   content_type='application/json')
        
        # Verificar que la sesion se creó correctamente
        self.assertEqual(response.status_code, 201, 
                        "La sesión debería crearse exitosamente")
        
        data = json.loads(response.data)
        self.assertEqual(data['mensaje'], 'Sesión creada correctamente')
        self.assertIsInstance(data['id'], int) 
        
        # Verificar que se llamó al método add con los parámetros correctos
        mock_service.add.assert_called_once()
        call_args = mock_service.add.call_args[0][0]  
        self.assertEqual(call_args.nombre, "Entrenamiento de Espalda")
        self.assertEqual(call_args.descripcion, "Sesion completa para fortalecer musculos dorsales")
        
        print("TEST CREACION DE SESION: Sesion creada exitosamente")

    @patch('routes.sesion_routes.service')
    def test_mostrar_todas_sesiones(self, mock_service):
        
        # Configurar mock del servicio
        # Crear mock de sesión con __dict__ como atributo
        mock_sesion = type('MockSesion', (), {
            '__dict__': {
                "id": 1,
                "nombre": "Entrenamiento de Pecho",
                "descripcion": "Sesion completa para fortalecer musculos pectorales",
                "estado": False
            }
        })()
        mock_service.list.return_value = [mock_sesion]
        
        # Enviar petición GET para obtener todas las sesiones
        response = self.client.get('/api/admin/sesiones')
        
        # Verificar que se obtuvieron las sesiones correctamente
        self.assertEqual(response.status_code, 200,
                        "Deberia obtener la lista de sesiones exitosamente")
        
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)  
        
        # Verificar que la estructura sea correcta
        if len(data) > 0:
            self.assertIn('nombre', data[0])
            self.assertIn('descripcion', data[0])
        
        # Verificar que se llamo al metodo list
        mock_service.list.assert_called_once()
        
        print("TEST OBTENCION DE TODAS LAS SESIONES: Lista de sesiones obtenida exitosamente")

    @patch('routes.sesion_routes.service')
    def test_mostrar_sesion_por_id(self, mock_service):
        
        # Configurar mock del servicio
        # Crear mock de sesion con __dict__ como atributo
        mock_sesion = type('MockSesion', (), {
            '__dict__': {
                "id": 1,
                "nombre": "Entrenamiento de Pecho",
                "descripcion": "Sesion completa para fortalecer musculos pectorales",
                "estado": False
            }
        })()
        mock_service.get_by_id.return_value = mock_sesion
        
        # Enviar peticion GET para obtener sesion por ID
        response = self.client.get('/api/admin/sesiones/1')
        
        # Verificar que se obtuvo la sesion correctamente
        self.assertEqual(response.status_code, 200,
                        "Deberia obtener la sesion por ID exitosamente")
        
        data = json.loads(response.data)
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertIn('nombre', data)
        self.assertEqual(data['id'], 1)
        
        # Verificar que se llamo al metodo get_by_id con el ID correcto
        mock_service.get_by_id.assert_called_once_with(1)
        
        print("TEST OBTENCION DE SESION POR ID: Sesion obtenida por ID exitosamente")

    @patch('routes.sesion_routes.service')
    def test_modificar_sesion(self, mock_service):
        
        # Configurar mock del servicio
        mock_service.update.return_value = "Sesión actualizada con éxito"
        
        # Enviar peticion PUT para actualizar sesion
        response = self.client.put('/api/admin/sesiones/1',
                                 json=self.sesion_actualizada_data,
                                 content_type='application/json')
        
        # Verificar que la sesion se actualizo correctamente
        self.assertEqual(response.status_code, 200,
                        "La sesion deberia actualizarse exitosamente")
        
        data = json.loads(response.data)
        self.assertEqual(data['mensaje'], 'Sesión actualizada con éxito')
        
        # Verificar que se llamo al metodo update
        mock_service.update.assert_called_once()
        call_args = mock_service.update.call_args[0][0]  # Primer argumento 
        self.assertEqual(call_args.nombre, "Entrenamiento de Pecho Avanzado")
        self.assertEqual(call_args.descripcion, "Sesion avanzada para pectoral superior e inferior")
        self.assertEqual(call_args.id, 1)
        
        print("TEST ACTUALIZACION DE SESION: Sesion actualizada exitosamente")

    @patch('routes.sesion_routes.service')
    def test_eliminar_sesion(self, mock_service):
        
        # Configurar mock del servicio
        mock_service.delete.return_value = "Sesión eliminada con éxito"
        
        # Enviar peticion DELETE para eliminar sesion
        response = self.client.delete('/api/admin/sesiones/1')
        
        # Verificar que la sesion se elimino correctamente
        self.assertEqual(response.status_code, 200,
                        "La sesion deberia eliminarse exitosamente")
        
        data = json.loads(response.data)
        self.assertEqual(data['mensaje'], 'Sesión eliminada con éxito')
        
        # Verificar que se llamo al metodo delete con el ID correcto
        mock_service.delete.assert_called_once_with(1)
        
        print("TEST ELIMINACION DE SESION: Sesion eliminada exitosamente")


def suite():
    """Crear suite de tests"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestSesionCRUD('test_crear_sesion'))
    test_suite.addTest(TestSesionCRUD('test_mostrar_todas_sesiones'))
    test_suite.addTest(TestSesionCRUD('test_mostrar_sesion_por_id'))
    test_suite.addTest(TestSesionCRUD('test_modificar_sesion'))
    test_suite.addTest(TestSesionCRUD('test_eliminar_sesion'))
    return test_suite


if __name__ == '__main__':
    print("\nTESTS CRUD DE SESIONES")
    print("\n - Crear sesion")
    print(" - Mostrar todas las sesiones")
    print(" - Mostrar sesion por ID")
    print(" - Modificar sesion")
    print(" - Eliminar sesion")
    print("=" * 60)
    
    # Cambiar al directorio padre para ejecutar
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir)
    
    # Ejecutar tests con unittest
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    
    print("\n" + "=" * 60)
    print("RESUMEN DE RESULTADOS:")
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