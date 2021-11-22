from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/logginn', methods=['GET', 'POST'])
def logginn():
    if request.method == 'POST':
        epost = request.form.get('epost')
        passord = request.form.get('passord')

        bruker = User.query.filter_by(epost=epost).first()
        if bruker:
            if check_password_hash(bruker.passord, passord):
                flash('Gratulerer! Da er du logget inn.', category='korrekt')
                login_user(bruker, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Passord er ikke korrekt. Prøv igjen.', category='feil')
        else:
            flash('Epostadressen ekstisterer ikke.', category='feil')

    return render_template("logginn.html", text="Testing", user=current_user)

@auth.route('/registrer_deg', methods=['GET', 'POST'])
def registrer_deg():
    if request.method == "POST":
        epost = request.form.get('epost')
        fornavn = request.form.get('fornavn')
        etternavn = request.form.get('etternavn')
        passord1 = request.form.get('passord1')
        passord2 = request.form.get('passord2')
        rolle = request.form.get('rolle')

        bruker = User.query.filter_by(epost=epost).first()

        if bruker:
            flash('Epostadressen eksisterer fra før.', category='feil')
        elif len(epost) < 4:
            flash('Epostadresse må være over 3 tegn.', category='feil')
        elif len(fornavn) < 2:
            flash('Fornavn må være over 1 tegn.', category='feil')
        elif len(etternavn) <= 2:
            flash('Etternavn må være over 2 tegn eller mer.', category='feil')
        elif passord1 != passord2:
            flash('Passord må være like.', category='feil')
        elif len(passord1) < 7:
            flash('Passord må være større enn 6 tegn, minimum 7.', category='feil')
        elif rolle != "Admin" or rolle != "Auksjonær" or rolle != "Butikkeier":
            flash('Rolle kan bare være Admin, Auksjonær eller Butikkeier')
        else:
            # legg til bruker i databasen
            ny_bruker = User(epost=epost, fornavn=fornavn, etternavn=etternavn, passord=generate_password_hash(passord1, method='sha256'), rolle=rolle)
            db.session.add(ny_bruker)
            db.session.commit()
            login_user(bruker, remember=True)
            flash('Konto opprettet!', category='korrekt')
            return redirect(url_for('views.home'))

    return render_template("registrer_deg.html", user=current_user)

@auth.route('/loggut')
@login_required
def loggut():
    logout_user()
    return redirect(url_for('auth.logginn'))



