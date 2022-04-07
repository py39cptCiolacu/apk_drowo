from flask import Blueprint, render_template, request, redirect, flash, url_for


auth = Blueprint('auth', __name__)

conturi = {'echipa1': 'parola1', 'echipa2': 'parola2'}

@auth.route('admin', methods = ['GET', 'POST'])
def admin():

    return render_template('admin.html')


@auth.route('/login_team', methods = ['GET', 'POST'])
def login_echipa():

    if request.method == 'POST':
        id_team = request.form.get('id_team')
        password_team = request.form.get('password_team')
        if id_team in conturi and conturi[id_team] == password_team:
            return redirect(url_for('views.team'))
        else:
            flash('Parola incorecta, incearca din nou', category='error')    

    return render_template('login_team.html')