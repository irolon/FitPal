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
from Model.Ejercicio import Ejercicio


class TestEjercicioCRUD(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        # Ejercicio de ejemplo para los tests
        self.ejercicio_ejemplo = Ejercicio(
            id=1,
            categoria="Pecho",
            nombre="Press de Banca",
            descripcion="Ejercicio para fortalecer pectorales",
            repeticiones=12,
            series=3,
            descanso=60
        )
        
        # Datos para crear un nuevo ejercicio
        self.nuevo_ejercicio_data = {
            "categoria": "Espalda",
            "nombre": "Dominadas",
            "descripcion": "Ejercicio para fortalecer dorsales",
            "repeticiones": 8,
            "series": 4,
            "descanso": 90
        }
        
        # Datos para actualizar un ejercicio
        self.ejercicio_actualizado_data = {
            "categoria": "Pecho",
            "nombre": "Press de Banca Inclinado",
            "descripcion": "Ejercicio para pectoral superior",
            "repeticiones": 10,
            "series": 4,
            "descanso": 75
        }

    @patch('routes.ejercicio_routes.EjercicioService')
    def test_crear_ejercicio(self, mock_service_class):
        
        # Configurar mock del servicio
        mock_service = MagicMock()
        mock_service.crear.return_value = 2  # ID del nuevo  del modelo ejercicio
        mock_service_class.return_value = mock_service
        
        # Enviar peticion POST para crear ejercicio
        response = self.client.post('/api/admin/ejercicios', 
                                  json=self.nuevo_ejercicio_data,
                                  content_type='application/json')
        
        # Verificar que el ejercicio se creo correctamente
        self.assertEqual(response.status_code, 201, 
                        "El ejercicio debería crearse exitosamente")
        
        data = json.loads(response.data)
        self.assertEqual(data['mensaje'], 'Ejercicio creado')
        self.assertIsInstance(data['id'], int)  # Solo verificar que sea un entero
        
        # Verificar que se llamo al metodo crear con los parametros correctos
        mock_service.crear.assert_called_once_with(
            categoria="Espalda",
            nombre="Dominadas", 
            descripcion="Ejercicio para fortalecer dorsales",
            repeticiones=8,
            series=4,
            descanso=90,
            estado="Activo"
        )
        
        print("TEST CREACION DE EJERCICIO: Ejercicio creado exitosamente")

    @patch('routes.ejercicio_routes.EjercicioService')
    def test_mostrar_todos_ejercicios(self, mock_service_class):
        
        # Configurar mock del servicio
        mock_service = MagicMock()
        mock_service.obtener_todos.return_value = [
            {
                "id": 1,
                "categoria": "Pecho",
                "nombre": "Press de Banca",
                "descripcion": "Ejercicio para fortalecer pectorales",
                "repeticiones": 12,
                "series": 3,
                "descanso": 60
            }
        ]
        mock_service_class.return_value = mock_service
        
        # Enviar peticion GET para obtener todos los ejercicios
        response = self.client.get('/api/ejercicios')
        
        # Verificar que se obtuvieron los ejercicios correctamente
        self.assertEqual(response.status_code, 200,
                        "Debería obtener la lista de ejercicios exitosamente")
        
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)  # Al menos debe haber ejercicios
        # Verificar que la estructura sea correcta
        if len(data) > 0:
            self.assertIn('nombre', data[0])
            self.assertIn('categoria', data[0])
        
        # Verificar que se llamo al metodo obtener_todos
        mock_service.obtener_todos.assert_called_once()
        
        print("TEST OBTENCION DE EJERCICIO POR ID: Lista de ejercicios obtenida exitosamente")

    @patch('routes.ejercicio_routes.EjercicioService')
    def test_mostrar_ejercicio_por_id(self, mock_service_class):
        
        # Configurar mock del servicio
        mock_service = MagicMock()
        mock_service.obtener_por_id.return_value = {
            "id": 1,
            "categoria": "Pecho",
            "nombre": "Press de Banca",
            "descripcion": "Ejercicio para fortalecer pectorales",
            "repeticiones": 12,
            "series": 3,
            "descanso": 60
        }
        mock_service_class.return_value = mock_service
        
        # Enviar peticion GET para obtener ejercicio por ID
        response = self.client.get('/api/ejercicios/1')
        
        # Verificar que se obtuvo el ejercicio correctamente
        self.assertEqual(response.status_code, 200,
                        "Debería obtener el ejercicio por ID exitosamente")
        
        data = json.loads(response.data)
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertIn('nombre', data)
        self.assertEqual(data['id'], 1)
        
        # Verificar que se llamo al metodo obtener_por_id con el ID correcto
        mock_service.obtener_por_id.assert_called_once_with(1)
        
        print("TEST OBTENCION DE EJERCICIO POR ID: Ejercicio obtenido por ID exitosamente")

    @patch('routes.ejercicio_routes.EjercicioService')
    def test_modificar_ejercicio(self, mock_service_class):
        
        # Configurar mock del servicio
        mock_service = MagicMock()
        mock_service.actualizar.return_value = True
        mock_service_class.return_value = mock_service
        
        # Enviar petición PUT para actualizar ejercicio
        response = self.client.put('/api/admin/ejercicios/1',
                                 json=self.ejercicio_actualizado_data,
                                 content_type='application/json')
        
        # Verificar que el ejercicio se actualizo correctamente
        self.assertEqual(response.status_code, 200,
                        "El ejercicio debería actualizarse exitosamente")
        
        data = json.loads(response.data)
        self.assertEqual(data['mensaje'], 'Ejercicio actualizado')
        
        # Verificar que se llamo al metodo actualizar con los parametros correctos
        mock_service.actualizar.assert_called_once_with(
            1,
            categoria="Pecho",
            nombre="Press de Banca Inclinado",
            descripcion="Ejercicio para pectoral superior", 
            repeticiones=10,
            series=4,
            descanso=75,
            estado=None
        )
        
        print("TEST ACTUALIZACION DE EJERCICIO: Ejercicio actualizado exitosamente")

    @patch('routes.ejercicio_routes.EjercicioService')
    def test_eliminar_ejercicio(self, mock_service_class):
        
        # Configurar mock del servicio
        mock_service = MagicMock()
        mock_service.eliminar.return_value = True
        mock_service_class.return_value = mock_service
        
        # Enviar peticion DELETE para eliminar ejercicio
        response = self.client.delete('/api/admin/ejercicios/1')
        
        # Verificar que el ejercicio se elimino correctamente
        self.assertEqual(response.status_code, 200,
                        "El ejercicio debería eliminarse exitosamente")
        
        data = json.loads(response.data)
        self.assertEqual(data['mensaje'], 'Ejercicio eliminado')
        
        # Verificar que se llamó al método eliminar con el ID correcto
        mock_service.eliminar.assert_called_once_with(1)
        
        print("TEST ELIMINACION DE EJERCICIO: Ejercicio eliminado exitosamente")





def suite():
    """Crear suite de tests"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestEjercicioCRUD('test_crear_ejercicio'))
    test_suite.addTest(TestEjercicioCRUD('test_mostrar_todos_ejercicios'))
    test_suite.addTest(TestEjercicioCRUD('test_mostrar_ejercicio_por_id'))
    test_suite.addTest(TestEjercicioCRUD('test_modificar_ejercicio'))
    test_suite.addTest(TestEjercicioCRUD('test_eliminar_ejercicio'))
    return test_suite


if __name__ == '__main__':
    print("\nTESTS CRUD DE EJERCICIOS")
    print("\n - Crear ejercicio")
    print(" - Mostrar todos los ejercicios")
    print(" - Mostrar ejercicio por ID")
    print(" - Modificar ejercicio")
    print(" - Eliminar ejercicio")
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
        print("\n¡TODOS LOS TESTS DE EJERCICIOS PASARON!")
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
    
