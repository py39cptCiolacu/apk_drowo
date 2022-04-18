from . import db
from flask_login import UserMixin


class Team(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    puncte = db.Column(db.Integer)
    name = db.Column(db.Integer)

    def __init__(self, username, password, puncte = 0, name = 'Echipa'):
        self.username = username
        self.password = password
        self.puncte = puncte
        self.name = name

    def change_name(self, name):
        self.name = name

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(150))
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    description = db.Column(db.String(200))
    colors = db.Column(db.String(50))

    def __init__(self, image, name, price, description, colors):
        self.price = price
        self.image = image
        self.colors = colors
        self.name = name
        self.description = description