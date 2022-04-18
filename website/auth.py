from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db
from website.models import Team
from flask_login import login_user, login_required, logout_user, current_user
 

auth = Blueprint('auth', __name__)


@auth.route('admin', methods = ['GET', 'POST'])
def admin():

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

    return render_template('admin.html', team = current_user)


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