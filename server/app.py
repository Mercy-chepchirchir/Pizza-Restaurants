from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_restful import Api,Resource
from models import db, Restaurant, Pizza, RestaurantPizza
from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'#specifies the URI for the sqlite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api= Api(app)#create an instance of the Flask-restful API extension 
[]
#define a new class home
#Resource class is used to define how different http methods shold be handled
class Home(Resource):
    def get(self):
        
        response_dict ={
            "message":"Welcome to PIzza Restaurant ",
        }
        
        response = make_response(
            response_dict,
            200    
        )
        return response
api.add_resource(Home, '/')

class Restaurants(Resource):
    def get(self):
        #initialize an empty list
        restaurants = []
        for restaurant  in Restaurant.query.all():
            #resturant_dict is used to store information about a single restaurant 
            restaurant_dict={
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
            restaurants.append(restaurant_dict)
        return make_response(jsonify(restaurants), 200)

api.add_resource(Restaurants,'/restaurants')  
 
