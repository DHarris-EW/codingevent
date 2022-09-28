from flask import Blueprint, flash, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import redirect

from website import bcrypt, db
from .models import User
from website.forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    print('hello')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(service_number=form.service_number.data, rank=form.rank.data, name=form.name.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.rank.data} {form.name.data}!', 'success')
        return redirect(url_for('user.login'))
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
