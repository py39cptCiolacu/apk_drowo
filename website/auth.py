from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db
from website.models import Team, Product 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route("admin", methods =['GET', 'POST'])
def admin():

    return render_template('admin.html', team = current_user)


@auth.route('admin_teams', methods = ['GET', 'POST'])
def admin_teams():

    ## creare conturi

    if request.method == 'POST':
        id_team = request.form.get('id_team')
        password_team = request.form.get('password_team')
        password_team_confirm = request.form.get('password_team_confirm')
        check = Team.query.filter_by(username = id_team).first()
        if password_team != password_team_confirm:
            flash('Parolele nu sunt la fel, incearca din nou', category='error')
        elif check:
            flash('Numele e luat deja', category='error')
        else:
            team = Team(username=id_team, password=password_team)
            db.session.add(team)
            db.session.commit()
            flash('Contul a fost creat cu succes', category='succes')
            return redirect(url_for('auth.login_team'))

    return render_template('admin_teams.html', team = current_user)

@auth.route("admin_obj_delete", methods =['GET', 'POST'])
def admin_obj_delete():

    
    products = Product.query.all()


    if request.method == 'POST':
        name = request.form.get('name')
        product_to_delete = Product.query.filter_by(name = name).first()
        if product_to_delete:
            db.session.delete(product_to_delete)
            db.session.commit()
        else:
            flash('Nu exista obiectul', category='error')

    return render_template('admin_obj_delete.html', team=current_user, products = products)


@auth.route("admin_obj", methods =['GET', 'POST'])
def admin_obj():

    if request.method == 'POST':
        obj_name = request.form.get('obj_name')
        obj_imag = request.form.get('obj_imag')
        obj_description = request.form.get('obj_description')
        obj_code = request.form.get('obj_code')
        obj_stoc = request.form.get('obj_stoc')
        check = Product.query.filter_by(name = obj_name).first()
        check2 = Product.query.filter_by(code = obj_code).first()
        if check:
            flash('Un produs cu acelasi nume exista deja', category='error')
        elif check2:
            flash('Un produs cu acest cod exista deja')
        else:
            product = Product(code = obj_code,image = obj_imag, name = obj_name, description= obj_description, stoc = int(obj_stoc))
            db.session.add(product)
            db.session.commit()
            flash('Produs adaugat', category='succes')

    return render_template('admin_obj.html', team = current_user)


@auth.route("admin_points", methods =['GET', 'POST'])
def admin_points():

    teams = Team.query.all()

    if request.method == 'POST':
        team_name = request.form.get('team_name')
        nr_points = request.form.get('nr_points')
        team = Team.query.filter_by(username = team_name).first()
        if not team:
            flash('Echipa nu exista', category='error')
        else:
            team.change_points(int(nr_points))
            db.session.commit()
            flash('Puncte Adaugate', category='succes')

    return render_template('admin_points.html', team = current_user, teams = teams)


@auth.route('/login_team', methods = ['GET', 'POST'])
def login_team():

    if request.method == 'POST':
        id_team = request.form.get('id_team')
        password_team = request.form.get('password_team')

        team = Team.query.filter_by(username = id_team).first()
        if id_team == 'admin' and password_team == 'adminparola':
            return redirect(url_for('auth.admin'))
        if team:
            if password_team == team.password:
                login_user(team, remember=True)
                flash('Autenficat cu succes', category='succes')
                return redirect(url_for('views.team'))
            else:
                flash('Parola incorecta', category='error')
        else:
            flash('Nume incorect', category='error')    

    return render_template('login_team.html', team=current_user)

@auth.route('/logout_team', methods = ['GET', 'POST'])
@login_required
def logout_team():
    logout_user()
    return redirect(url_for('auth.login_team'))