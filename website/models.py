from flask_login import UserMixin
from sqlalchemy.sql import func

from website import db


class Logginn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    epost = db.Column(db.String(150), unique=True)
    passord = db.Column(db.String(120))
    fornavn = db.Column(db.String(100))
    etternavn = db.Column(db.String(150))
    rolle = db.Column(db.String(150))
    datetime = db.Column(db.DateTime(timezone=True), default=func.now())
    innlogginger = db.relationship('Logginn')
