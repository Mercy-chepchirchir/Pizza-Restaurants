import unittest
import json
from app import app, db, Restaurant, Pizza, RestaurantPizza

class TestPizzaRestaurantAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_restaurants(self):
        # Create some test restaurants
        restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
        restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")
        db.session.add(restaurant1)
        db.session.add(restaurant2)
        db.session.commit()

        response = self.app.get('/restaurants')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_single_restaurant(self):
        # Create a test restaurant and associated pizzas
        restaurant = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
        pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
        pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        restaurant_pizza1 = RestaurantPizza(price=10, restaurant=restaurant, pizza=pizza1)
        restaurant_pizza2 = RestaurantPizza(price=12, restaurant=restaurant, pizza=pizza2)
        db.session.add(restaurant)
        db.session.add(pizza1)
        db.session.add(pizza2)
        db.session.add(restaurant_pizza1)
        db.session.add(restaurant_pizza2)
        db.session.commit()

        response = self.app.get('/restaurants/1')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], "Dominion Pizza")
        self.assertEqual(len(data['pizzas']), 2)

    def test_delete_restaurant(self):
        # Create a test restaurant
        restaurant = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
        db.session.add(restaurant)
        db.session.commit()

        response = self.app.delete('/restaurants/1')
        self.assertEqual(response.status_code, 204)

        # Verify the restaurant has been deleted
        deleted_restaurant = Restaurant.query.get(1)
        self.assertIsNone(deleted_restaurant)

if __name__ == '__main__':
    unittest.main()
