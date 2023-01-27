import json
import unittest
from flask import Flask
from flask_testing import TestCase

class TodoAPITestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.client = self.app.test_client()

    def test_get_todos(self):
        response = self.client.get('/todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {'todos': []})

    def test_add_todo(self):
        response = self.client.post('/todos', data=json.dumps({'task': 'test todo'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {'todos': [{'task': 'test todo'}]})

    def test_update_todo(self):
        self.client.post('/todos', data=json.dumps({'task': 'test todo'}), content_type='application/json')
        response = self.client.put('/todos/0', data=json.dumps({'task': 'updated todo'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {'todos': [{'task': 'updated todo'}]})

    def test_delete_todo(self):
        self.client.post('/todos', data=json.dumps({'task': 'test todo'}), content_type='application/json')
        response = self.client.delete('/todos/0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {'todos': []})

if __name__ == '__main__':
    unittest.main()