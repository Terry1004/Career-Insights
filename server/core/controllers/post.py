from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.post import Post


bluePrint = Blueprint('post', __name__, url_prefix='/post')


@bluePrint.route('/', methods=['GET'])
def index():
    posts = Post.fetchall()
    return render_template('post/index.html', posts=posts)


@bluePrint.route('/<post_id>', methods=['GET'])
def detail(post_id):
    post = Post.find_by_id(post_id)
    if post:
        return render_template('post/detail.html', post=post)
    else:
        return render_template('error/404.html', message='Post Not Found.')
