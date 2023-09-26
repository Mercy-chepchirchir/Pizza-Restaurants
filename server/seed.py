from random import  choice as rc, sample
from faker import Faker
from app import app
from models import db, Restaurant, RestaurantPizza, Pizza
import random

#defined a list of the restaurant names
restaurantnames = [    
    "The Savory Spoon",
    "Fireside Bistro",
    "The Hungry Hound",
    "Spice and Vine",
    "Fork & Knife",
    "Tastes of Tuscany",
    "The Wholesome Plate",
    "Munchies & More",
    "Coastal Catch",
    "The Gourmet Garden",
    "Sizzle & Smoke",
    "Flavor Fusion",
    "The Rustic Retreat",
    "Zesty Delights",
    "The Urban Grill",
    "Crispy Crust Pizzeria",
    "The Sizzling Skillet",
    "The Secret Ingredient",
    "Sweet Tooth Treats",
    "Fusion Feast",
    "The Spice Route",
    "Farmhouse Fare",
    "Delish Delights",
    "The Olive Branch",
    "Tacos & Tequila",
    "The Daily Grind",
    "The Green Leaf Cafe",
    "Sugar & Spice Bakery",
    "Bite Me Burgers",
    "The Cozy Corner",
]
#defined a list of ingredients
ingredients = [
    "Pepperoni",
    "Mushrooms",
    "Bell peppers",
    "Onions",
    "Black olives",
    "Sausage",
    "Fresh basil",
    "Pineapple",
    "Ham",
    "Spinach",
    "Feta cheese",
    "Sun-dried tomatoes",
    "Anchovies",
    "Arugula",
    "Provolone cheese",
    "Artichoke hearts",
    "Goat cheese",
    "Garlic",
    "Jalapeños",
    "Ricotta cheese",
    "Red pepper flakes",
    "Fresh tomatoes",
    "Bacon",
    "Mozzarella cheese",
    "Fresh oregano",
    "Capers",
    "Chicken",
    "Parmesan cheese",
    "Gorgonzola cheese",
    "Fresh cilantro",
]

fake = Faker()
# a context manager to ensure database operations occur within the application context
with app.app_context():
    #delete existing data from tables
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()
