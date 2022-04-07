from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():

    return render_template('home.html')


@views.route('team', methods = ['GET', 'POST'])
def team():

    return render_template('team.html')