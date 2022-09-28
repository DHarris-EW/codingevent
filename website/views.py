from flask import Blueprint, render_template, flash, jsonify
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


