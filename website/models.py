from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    service_number = db.Column(db.String(8), unique=True, nullable=False)
    rank = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)


class AinU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nsn = db.Column(db.String(), nullable=False)
    serial_number = db.Column(db.String(), nullable=False)
    owner = db.Column(db.String(50), nullable=False)
    image = db.Column(db.Text, nullable=False)
