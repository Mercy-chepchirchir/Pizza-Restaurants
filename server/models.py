from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    serialize_rules = ('-pizzas.restaurant','-restaurant.pizzas')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable= False,unique= True)
    address = db.Column(db.String)
    
    pizzas = db.relationship('RestaurantPizza',backref='restaurants')
    
    @validates("name")
    def validate_name(self, key, name):
        if  len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        return name
    
