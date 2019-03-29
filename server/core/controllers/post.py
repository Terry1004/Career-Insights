from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)


bluePrint = Blueprint('post', __name__, url_prefix='/post')


@bluePrint.route('/', methods=['GET'])
def index():
    return render_template('post/index.html')
