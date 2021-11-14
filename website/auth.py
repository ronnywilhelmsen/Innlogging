from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/logginn')
def logginn():
    return "<p>Logget inn<p>"

@auth.route('/loggut')
def loggut():
    return "<p>Logget ut<p>"

@auth.route('/registrer_deg')
def registrer_deg():
    return "<p>Registrer deg<p>"

