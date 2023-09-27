import unittest
from flask import Flask
from app import db, Restaurant, Pizza, RestaurantPizza

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_endpoint(self):
        with self.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], 'Welcome to Pizza Restaurant')

    def test_get_restaurants(self):
        with self.app.test_client() as client:
            with self.app.app_context():
                restaurant = Restaurant(name='Test Restaurant', address='Test Address')
                db.session.add(restaurant)
                db.session.commit()

            response = client.get('/restaurants')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]['name'], 'Test Restaurant')

    # Add other test methods...

if __name__ == '__main__':
    unittest.main()