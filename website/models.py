from . import db



class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    puncte = db.Column(db.Integer)
    names = db.Column(db.Integer)

    def __init__(self, username, password, puncte = 0, names = 'A/B/C/D/E/F'):
        self.username = username
        self.password = password
        self.puncte = puncte
        self.names = names