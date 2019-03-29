from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.user import User
from .auth import login_required


blueprint = Blueprint('profile', __name__, url_prefix='/profile')


@blueprint.route('/', methods=['GET'])
@login_required
def index():
    uni = session['uni']
    user = User.find_by_uni(uni)
    if user:
        return render_template('profile/index.html', user=user)
    else:
        return render_template('error/404.html', message='User Not Found.')


@blueprint.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    uni = session['uni']
    if request.method == 'POST':
        error = None
        password = request.form['password']
        email = request.form['email']
        personal_des = request.form['personal_des']
        username = request.form['username']
        major = request.form['major']
        if not password:
            error = 'Password cannot be empty.'
        if not error:
            user = User(uni, password, email, personal_des, username, major)
            user.save(update=True)
            return redirect(url_for('profile.index'))
        flash(error)
    user = User.find_by_uni(uni)
    if user:
            return render_template('profile/edit.html', user=user)
    else:
        return render_template('error/404.html', message='User Not Found.')
