from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from . import db
from website.models import Product


views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():

    product = Product(image = 'x', price = 20, description='da', name ='produs1', colors = 'red')
    db.session.add(product)
    db.session.commit()
    product = Product(image = 'x', price = 20, description='da', name ='produs2', colors = 'red')
    db.session.add(product)
    db.session.commit()

    return render_template('home.html', team = current_user)


@views.route('team', methods = ['GET', 'POST'])
@login_required
def team():

    if request.method == 'POST':
        name = request.form.get('id_team')
        current_user.change_name(name)
        #db.session.update()
        db.session.commit()

        flash('Nume actualizate', category='succes')

    return render_template('team.html', team = current_user)

@views.route('shop', methods = ['GET', 'POST'])
@login_required
def shop():

    products = Product.query.all()

    return render_template('shop.html', team = current_user, products = products)