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

    config_code = current_user.config
    frame_code = current_user.frame

    config = Product.query.filter_by(code = config_code).first()
    frame = Product.query.filter_by(code = frame_code).first()

    if request.method == 'POST':
        name = request.form.get('id_team')
        color = request.form.get('color_team')
        current_user.change_name(name)
        current_user.change_color(color)
        #db.session.update()
        db.session.commit()
        flash('Nume actualizat', category='succes')

    return render_template('team.html', team = current_user, config=config, frame=frame)

@views.route('shop', methods = ['GET', 'POST'])
@login_required
def shop():

    products = Product.query.all()

    if request.method == "POST":
        code = request.form.get('button')
        obj = Product.query.filter_by(code = code).first()
        if obj.stoc == 0:
            flash('Acest obiect nu se mai afla pe stoc', category='error')
        if code.startswith('FRAME'):
            current_user.add_cart_frame(code)
            db.session.commit()
        if code.startswith('CONFIG'):
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

    print(config_cart, frame_cart)

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
                 return redirect(url_for('views.shop_cart'))
            elif current_user.points < (config_cart.price + frame_cart.price):
                flash('Nu ai suficiente puncte', category='error')  
                return redirect(url_for('views.shop_cart'))
            elif config_cart.stoc == 0 or frame_cart == 0:
                flash('Unul din produsele din cos nu mai este pe stoc', category='error')
                return redirect(url_for('views.shop_cart'))         
            elif current_user.cart_frame != '' and current_user.cart_config != '':
                current_user.add_config(current_user.cart_config)
                current_user.add_frame(current_user.cart_frame)
                current_user.add_cart_frame('')
                current_user.add_cart_config('')
                current_user.change_points(current_user.points - (config_cart.price + frame_cart.price))
                config_cart.change_stoc(config_cart.stoc - 1)
                db.session.commit()
                return redirect(url_for('views.team'))


    return render_template('shop_cart.html', team = current_user, config_cart=config_cart, frame_cart=frame_cart)
