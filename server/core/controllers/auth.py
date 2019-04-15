from functools import wraps

from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
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
        uni = request.form['uni'].strip()
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        email = request.form['email'].strip()
        username = request.form['username'].strip()
        major = request.form['major'].strip()
        personal_des = request.form['personal_des'].strip()
        error = False
        if not uni:
            flash('UNI is required.')
            error = True
        if not password:
            flash('Password is required.')
            error = True
        if not password_confirm:
            flash('Confirmation of password is required.')
            error = True
        if password != password_confirm:
            flash('The passwords entered are different.')
            error = True
        if not email:
            flash('Email is required.')
            error = True
        if not username:
            flash('Username is required.')
            error = True
        if not error:
            user = User.find_by_uni(uni)
            if not user:
                user = User(
                    uni, password, email, personal_des, username, major
                )
                user.save()
            else:
                flash('This UNI has already been registered.')
                error = True
        if error:
            return redirect('')
        else:
            return redirect(url_for('auth.login'))
    return render_template(
        'auth/register.html', path=[('#', 'Sign Up')], curr_tab='Sign Up'
    )


@blueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        uni = request.form['uni'].strip()
        password = request.form['password']
        error = False
        if not uni:
            flash('UNI is required.')
            error = True
        if not password:
            flash('Password is required.')
            error = True
        user = User.find_by_uni(uni)
        if not user:
            flash('UNI not found.')
            error = True
        elif not check_password_hash(user.password, password):
            flash('Incorrect password.')
            error = True
        if error:
            return redirect('')
        else:
            session.clear()
            session['uni'] = user.uni
            session['username'] = user.username
            return redirect(url_for('index'))
    return render_template(
        'auth/login.html', path=[('#', 'Sign In')], curr_tab='Sign In'
    )


@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@blueprint.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    uni = session['uni']
    user = User.find_by_uni(uni)
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        new_password_confirm = request.form['new_password_confirm']
        error = False
        if not old_password:
            flash('Old password is required.')
            error = True
        if not new_password:
            flash('New password is required.')
            error = True
        if not new_password_confirm:
            flash('Confirmation of new password is required.')
            error = True
        if not check_password_hash(user.password, old_password):
            flash('Incorrect old password.')
            error = True
        if new_password != new_password_confirm:
            flash('New passwords entered are different.')
            error = True
        if error:
            return redirect('')
        else:
            user.password = generate_password_hash(new_password)
            user.save(update=True)
            return redirect(url_for('profile.index'))
    return render_template(
        'auth/change-password.html',
        path=[('/profile', user.username), ('#', 'Change Password')],
        curr_tab='Profile'
    )
