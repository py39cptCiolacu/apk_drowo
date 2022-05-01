from tkinter import Frame
from . import db
from flask_login import UserMixin


class Team(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    points = db.Column(db.Integer)
    name = db.Column(db.Integer)
    cart_frame = db.Column(db.String(100))
    cart_config = db.Column(db.String(100))
    frame = db.Column(db.String(100))
    config = db.Column(db.String(100))

    def __init__(self, username, password, points = 0, name = 'Echipa', cart_frame ='', cart_config= '', frame ='', config = ''):
        self.username = username
        self.password = password
        self.points = points
        self.name = name
        self.cart_frame = cart_frame
        self.cart_config = cart_config
        self.frame = frame
        self.config = config

    def change_name(self, name):
        self.name = name

    def change_points(self, points):
        self.points = points

    def add_cart_frame(self, new_prod):
        self.cart_frame =  new_prod

    def add_cart_config(self, new_prod):
        self.cart_config =  new_prod

    def add_frame(self, new_prod):
        self.frame =  new_prod

    def add_config(self, new_prod):
        self.config =  new_prod

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(150))
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    description = db.Column(db.String(200))
    code = db.Column(db.String(100))

    def __init__(self, image, name, description, code):
        self.price = int(code[-2:])
        self.image = image
        self.name = name
        self.description = description
        self.code = code