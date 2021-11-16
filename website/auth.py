from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/logginn')
def logginn():
    return render_template("logginn.html", text="Testing")

@auth.route('/registrer_deg')
def registrer_deg():
    return render_template("registrer_deg.html")

@auth.route('/loggut')
def loggut():
    return "<h1> Logget ut. <h1>"



