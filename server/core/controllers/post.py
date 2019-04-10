from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.post import Post
from ..models.tag import Tag
from .auth import login_required


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


@bluePrint.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    if request.method == 'POST':
        uni = session['uni']
        title = request.form['title']
        content = request.form['content']
        post_type = request.form['post_type']
        rate = request.form['rate']
        position = request.form['position']
        company = request.form['company']
        hashtags = request.form['hashtags'].split(',')
        domain = request.form['domain']
        post_id = Post.get_max_id() + 1
        post = Post(uni, title, content, post_id=post_id)
        tag = Tag(
            post_id, post_type, rate, position, company, hashtags, domain
        )
        post.save()
        tag.save()
        return redirect(url_for('post.detail', post_id=post_id))
    return render_template('post/add-post.html')
