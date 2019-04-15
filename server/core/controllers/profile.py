import re
from flask import (
    Blueprint, redirect, render_template,
    request, flash, session, url_for, abort
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
        return render_template(
            'profile/index.html', user=user, uni=uni,
            path=[('#', user.username)], curr_tab='Profile'
        )
    else:
        abort(404)


@blueprint.route('/view/<uni>', methods=['GET'])
@login_required
def view(uni):
    user = User.find_by_uni(uni)
    uni = session['uni']
    if user.uni == uni:
        return redirect(url_for('profile.index'))
    elif user:
        return render_template(
            'profile/index.html', user=user, uni=uni,
            path=[('#', user.username)]
        )
    else:
        abort(404)


@blueprint.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    uni = session['uni']
    user = User.find_by_uni(uni)
    if request.method == 'POST':
        user.email = request.form['email']
        user.personal_des = request.form['personal_des']
        user.username = request.form['username']
        user.major = request.form['major']
        error = False
        if not user.email:
            flash('Email is required.')
            error = True
        elif not re.fullmatch(r'[^@]*@[^@]*', user.email):
            flash('Invalid email address.')
            error = True
        if error:
            return redirect('')
        else:
            user.save(update=True)
            return redirect(url_for('profile.index'))
    return render_template(
        'profile/edit.html', user=user,
        path=[
            ('/profile', user.username),
            ('#', 'Edit Profile')
        ],
        curr_tab='Profile'
    )
