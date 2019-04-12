from flask import (
    Blueprint, redirect, render_template,
    request, flash, session, url_for, abort
)
from ..models.post import Post
from ..models.tag import Tag
from ..models.comment import Comment
from .auth import login_required


blueprint = Blueprint('post', __name__, url_prefix='/post')


@blueprint.route('/', methods=['GET'])
def index():
    posts = Post.fetchall()
    return render_template('post/index.html', posts=posts)


@blueprint.route('/<post_id>', methods=['GET'])
def detail(post_id):
    post = Post.find_by_id(post_id)
    comments = Comment.fetchall(post_id)
    if 'uni' in session:
        uni = session['uni']
    else:
        uni = None
    if post:
        return render_template(
            'post/detail.html', post=post, uni=uni, comments=comments
        )
    else:
        abort(404)


@blueprint.route('/add-post', methods=['GET', 'POST'])
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
    return render_template('post/add-post.html', post=None)


@blueprint.route('/edit-post/<post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.find_by_id(post_id)
    tag = post.tag
    if post.uni != session['uni']:
        abort(403)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        tag.post_type = request.form['post_type']
        tag.rate = request.form['rate']
        tag.position = request.form['position']
        tag.company = request.form['company']
        tag.hashtags = request.form['hashtags'].split(',')
        tag.domain = request.form['domain']
        post.save(update=True)
        tag.save(update=True)
        return redirect(url_for('post.detail', post_id=post_id))
    return render_template('post/add-post.html', post=post)


@blueprint.route('/delete-post', methods=['POST'])
@login_required
def delete_post():
    post_id = request.form['post_id']
    post = Post.find_by_id(post_id)
    if post.uni != session['uni']:
        abort(403)
    else:
        post.destroy()
        return redirect(url_for('post.index'))
