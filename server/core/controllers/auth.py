from functools import wraps

from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from werkzeug.security import check_password_hash
from ..models.user import User


blueprint = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'uni' not in session:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uni = request.form['uni']
        email = request.form['email']
        password = request.form['password']
        error = None
        if not uni:
            error = 'UNI is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = User.findByUni(uni)
            if not user:
                user = User(uni, email, password)
                user.save()
                return redirect(url_for('auth.login'))
            else:
                error = 'This UNI has already been registered.'
        flash(error)
    return render_template('auth/register.html')


@blueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        uni = request.form['uni']
        password = request.form['password']
        user = User.findByUni(uni)
        error = None
        if not user:
            error = 'UNI not found.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect Password.'
        if error is None:
            session.clear()
            session['uni'] = user.uni
            print(f'User: {user.uni} login Successful')
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')


@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))