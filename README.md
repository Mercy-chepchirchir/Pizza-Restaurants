# Pizza-Restaurants
The Pizza Restaurant API is a Flask-based web service that allows users to interact with a database of restaurants and pizzas. It provides various endpoints for creating, retrieving, updating, and deleting restaurant and pizza information.

## Table of content
* Installation requirement
* Technology used
* Models
* Validations
* Routes
* Licence
* Authors info


# INSTALLATION PROCESS

* Git clone the repository to your local machine using the command `https://github.com/Mercy-chepchirchir/Pizza-Restaurants`
* Navigate to the code challenge directory using `cd Pizza-Restaurants `
* To install the necessary dependencies run `pipenv install`,`pip install sqlalchemy`,`pip install flask`,`pip install flask-migrate`,`pip install sqlalchemy_serializer `
* Install the requirement packages using pip
`pip install sqlalchemy faker`

# MODELS
* Restaurant: Represents a restaurant with attributes such as name and address.
* Pizza: Represents a pizza with attributes like name and ingredients.
* RestaurantPizza: Represents the relationship between restaurants and pizzas, including the price.

# VALIDATIONS
* RestaurantPizza: Price must be between 1 and 30.
* Restaurant: Must have a name less than 50 characters and must be unique.

# ROUTES
The API exposes the following routes:

* GET /restaurants: Returns a list of restaurants in JSON format.
* GET /restaurants/:id: Returns information about a specific restaurant along with its pizzas.
* DELETE /restaurants/:id: Deletes a restaurant and its associated restaurant-pizzas.
* GET /pizzas: Returns a list of pizzas in JSON format.
* POST /restaurant_pizzas: Creates a new restaurant-pizza association.

# TECHNOLOGY USED
python


# LICENSE
MIT license

# AUTHORS INFO
Mercy Chepchirchir

