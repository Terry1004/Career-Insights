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
    pass
