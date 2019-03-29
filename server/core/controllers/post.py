from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.post import Post


bluePrint = Blueprint('post', __name__, url_prefix='/post')


@bluePrint.route('/', methods=['GET'])
def index():
    posts = Post.fetchall()
    return render_template('post/index.html', posts=posts)
