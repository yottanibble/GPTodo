import unittest
import json
import requests

class TodoAPITestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000"
        self.todo = {"task": "run tests"}

    def test_get_todos(self):
        response = requests.get(f'{self.base_url}/todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_add_todo(self):
        response = requests.post(f'{self.base_url}/todos', json=self.todo)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['content-type'], 'application/json')
        self.assertEqual(response.json()['task'], 'run tests')

    def test_update_todo(self):
        response = requests.put(f'{self.base_url}/todos/1', json={"task": "updated task"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], 'application/json')
        self.assertEqual(response.json()['task'], 'updated task')

    def test_delete_todo(self):
        response = requests.delete(f'{self.base_url}/todos/1')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers['content-type'], 'application/json')

if __name__ == '__main__':
    unittest.main()