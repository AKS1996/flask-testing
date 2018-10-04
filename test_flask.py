import unittest
from app import app, db
import json


class TestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_hello_get(self):
        res = self.client().get('/hello')
        self.assertEqual(res.status_code, 200)
        self.assertIn('hello', str(res.data))

    def test_hello_post(self):
        res = self.client().post('/hello', data=json.dumps(dict(name='akshay')),
                       content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('hello akshay', str(res.data))

    def test_insert_task(self):
        res = self.client().post('/insert', data=json.dumps(dict(name='task1')),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()