from flask import Blueprint, render_template, flash, request, redirect,url_for
from flask_login import login_required, current_user
from . import db
from website.models import Product


views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():

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

    if request.method == "POST":
        code = request.form.get('button')
        #obj = Product.query.filter_by(code = code).first()
        if code.startswith('CONFIG'):
            current_user.add_cart_frame(code)
            db.session.commit()
        if code.startswith('FRAME'):
            current_user.add_cart_config(code)
            db.session.commit()

        

    return render_template('shop.html', team = current_user, products = products)


@views.route('shop_cart', methods = ['GET', 'POST'])
@login_required
def shop_cart():

    config_cart_code = current_user.cart_config
    frame_cart_code = current_user.cart_frame

    print(config_cart_code, frame_cart_code)

    config_cart = Product.query.filter_by(code = config_cart_code).first()
    frame_cart = Product.query.filter_by(code = frame_cart_code).first()

    #print(config_cart, frame_cart)

    if not config_cart:
        config_cart = 'null'
    if not frame_cart:
        frame_cart = 'null'


    if request.method == 'POST':
        check = request.form.get('button')
        if check == 'config':
            current_user.add_cart_config('')
            db.session.commit()
            return redirect(url_for('views.shop_cart'))
        if check == 'frame':
            current_user.add_cart_frame('')
            db.session.commit()
            return redirect(url_for('views.shop_cart'))
        if check == 'confirm':
            config_cart = Product.query.filter_by(code = config_cart_code).first()
            frame_cart = Product.query.filter_by(code = frame_cart_code).first()
            if current_user.cart_frame == '' or current_user.cart_config == '':
                 flash('Nu ai ambele obiecte in cos', category='error')
            elif current_user.points < (config_cart.price + frame_cart.price):
                flash('Nu ai suficiente puncte', category='error')           
            elif current_user.cart_frame != '' and current_user.cart_config != '':
                current_user.add_config(current_user.cart_config)
                current_user.add_frame(current_user.cart_frame)
                current_user.add_cart_frame('')
                current_user.add_cart_config('')
                current_user.change_points(current_user.points - (config_cart.price + frame_cart.price))
                db.session.commit()
                return redirect(url_for('views.shop_cart'))


    return render_template('shop_cart.html', team = current_user, config_cart=config_cart, frame_cart=frame_cart)
