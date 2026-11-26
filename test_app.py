
## @file test_app.py
# @brief Pruebas unitarias para la aplicación Flask.
# @details Verifica el comportamiento correcto del endpoint /hello ante peticiones válidas.

import unittest
from app import app


class TestApp(unittest.TestCase):

    ## @brief Configuración inicial del cliente de pruebas HTTP.
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    ## @brief Prueba el retorno de estado HTTP 200 y el saludo por defecto.
    def test_hello_endpoint(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data)


if __name__ == '__main__':
    unittest.main()

