from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.user import User
from .auth import login_required


blueprint = Blueprint('profile', __name__, url_prefix='/profile')


@blueprint.route('/', methods=['GET'])
@login_required
def profile():
    uni = session['uni']
    user = User.findByUni(uni)
    return render_template('profile/index.html', user=user)


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
        if error:
            flash(error)
            user = User.findByUni(uni)
            return render_template('profile/edit.html', user=user)
        else:
            user = User(uni, password, email, personal_des, username, major)
            user.save(update=True)
        return redirect(url_for('profile.profile'))
    else:
        user = User.findByUni(uni)
        return render_template('profile/edit.html', user=user)
