import json
import unittest
import sqlite3
from boenergo1 import app, conn

class EquationSolverTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Очистка базы данных перед каждым тестом
        with app.app_context():
            cursor = conn.cursor()
            cursor.execute('DELETE FROM equations')
            conn.commit()

        # Решение квадратного уравнения для тестирования
        data = {
            'a': 1,
            'b': -3,
            'c': 2
        }
        self.app.post('/equations', json=data)

    def test_solve_equation(self):
        data = {
            'a': 2,
            'b': -5,
            'c': -3
        }
        response = self.app.post('/equations', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data, {'roots': [3.0, -0.5]})

    def test_get_equations(self):
        response = self.app.get('/equations')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(response_data), 1)

if __name__ == '__main__':
    unittest.main()
