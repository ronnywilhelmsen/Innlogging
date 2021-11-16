from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/logginn', methods=['GET', 'POST'])
def logginn():
    data = request.form
    return render_template("logginn.html", text="Testing")

@auth.route('/registrer_deg', methods=['GET', 'POST'])
def registrer_deg():
    if request.method == "POST":
        epost = request.form.get('epost')
        fornavn = request.form.get('fornavn')
        etternavn = request.form.get('etternavn')
        passord1 = request.form.get('passord1')
        passord2 = request.form.get('passord2')

        if len(epost) < 4:
            flash('Epostadresse må være over 3 tegn.', category='feil')
        elif len(fornavn) < 2:
            flash('Fornavn må være over 1 tegn.', category='feil')
        elif len(etternavn) <= 2:
            flash('Etternavn må være over 2 tegn eller mer.', category='feil')
        elif passord1 != passord2:
            flash('Passord må være like.', category='feil')
        elif len(passord1) < 7:
            flash('Passord må være større enn 6 tegn, minimum 7.', category='feil')
        else:
            # legg til bruker i databasen
            flash('Konto opprettet!', category='korrekt')

    return render_template("registrer_deg.html")

@auth.route('/loggut')
def loggut():
    return "<h1> Logget ut. <h1>"



