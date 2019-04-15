from flask import (
    Blueprint, redirect, render_template,
    request, flash, session, url_for, abort
)
from ..models.post import Post
from ..models.tag import Tag
from ..models.comment import Comment
from .auth import login_required
from ..utils import non_empty_items


blueprint = Blueprint('post', __name__, url_prefix='/post')


@blueprint.route('/', methods=['GET'])
def index():
    internship_type = 'Internship Experience'
    fulltime_type = 'Full-time Experience'
    interview_type = 'Interview Experience'
    internship_posts = Post.fetchall(internship_type, recent=3)
    fulltime_posts = Post.fetchall(fulltime_type, recent=3)
    interview_posts = Post.fetchall(interview_type, recent=3)
    return render_template(
        'post/index.html',
        internship_posts=internship_posts,
        fulltime_posts=fulltime_posts,
        interview_posts=interview_posts,
        path=[],
        curr_tab='Forum'
    )


@blueprint.route('/Internship Experience', methods=['GET'])
def internship():
    post_type = 'Internship Experience'
    posts = Post.fetchall(post_type)
    return render_template(
        'post/posts.html', posts=posts, post_type=post_type,
        path=[('#', 'Internship Experience')], curr_tab='Forum'
    )


@blueprint.route('/Full-time Experience', methods=['GET'])
def fulltime():
    post_type = 'Full-time Experience'
    posts = Post.fetchall(post_type)
    return render_template(
        'post/posts.html', posts=posts, post_type=post_type,
        path=[('#', 'Full-time Experience')], curr_tab='Forum'
    )


@blueprint.route('/Interview Experience', methods=['GET'])
def interview():
    post_type = 'Interview Experience'
    posts = Post.fetchall(post_type)
    return render_template(
        'post/posts.html', posts=posts, post_type=post_type,
        path=[('#', 'Interview Experience')], curr_tab='Forum'
    )


@blueprint.route('/<int:post_id>', methods=['GET'])
def detail(post_id):
    post = Post.find_by_id(post_id)
    comments = Comment.fetchall(post_id)
    if 'uni' in session:
        uni = session['uni']
    else:
        uni = None
    if post:
        return render_template(
            'post/detail.html', post=post, uni=uni, comments=comments,
            path=[
                ('/post/{}'.format(post.tag.post_type), post.tag.post_type),
                ('#', post.title)
            ],
            curr_tab='Forum'
        )
    else:
        abort(404)


@blueprint.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    if request.method == 'POST':
        uni = session['uni']
        post_type = request.form['post_type']
        title = request.form['title'].strip()
        content = request.form['content'].strip()
        company = request.form['company'].strip()
        rate = request.form['rate']
        position = request.form['position'].strip()
        hashtags = non_empty_items(request.form['hashtags'].strip().split(','))
        domain = request.form['domain'].strip()
        error = False
        if not title:
            flash('Title is required.')
            error = True
        if not content:
            flash('Content is required.')
            error = True
        if not company:
            flash('Company is required.')
            error = True
        if not rate:
            flash('Rate is required.')
            error = True
        try:
            rate = int(rate)
            if not 1 <= rate <= 5:
                flash('Rate must be between 1 and 5.')
                error = True
        except ValueError:
            flash('Rate must be an integer.')
            error = True
        if not position:
            flash('Position is required.')
            error = True
        if error:
            return redirect('?post-type={}'.format(post_type))
        else:
            post_id = Post.get_max_id() + 1
            post = Post(uni, title, content, post_id=post_id)
            tag = Tag(
                post_id, post_type, rate, position, company, hashtags, domain
            )
            post.save()
            tag.save()
            return redirect(url_for('post.detail', post_id=post_id))
    post_type = request.args['post-type']
    return render_template(
        'post/add-post.html', post=None, post_type=post_type,
        path=[
            ('/post/{}'.format(post_type), post_type),
            ('#', 'New Post')
        ],
        curr_tab='Forum'
    )


@blueprint.route('/edit-post/<post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.find_by_id(post_id)
    tag = post.tag
    if post.uni != session['uni']:
        abort(403)
    if request.method == 'POST':
        tag.post_type = request.form['post_type']
        post.title = request.form['title']
        post.content = request.form['content']
        tag.company = request.form['company']
        tag.rate = request.form['rate']
        tag.position = request.form['position']
        tag.hashtags = non_empty_items(request.form['hashtags'].split(','))
        tag.domain = request.form['domain']
        error = False
        if not post.title:
            flash('Title is required.')
            error = True
        if not post.content:
            flash('Content is required.')
            error = True
        if not tag.company:
            flash('Company is required.')
            error = True
        if not tag.rate:
            flash('Rate is required.')
            error = True
        try:
            rate = int(tag.rate)
            if not 1 <= rate <= 5:
                flash('Rate must be between 1 and 5.')
                error = True
        except ValueError:
            flash('Rate must be an integer.')
            error = True
        if not tag.position:
            flash('Position is required.')
            error = True
        if error:
            return redirect('')
        else:
            post.save(update=True)
            tag.save(update=True)
            return redirect(url_for('post.detail', post_id=post_id))
    return render_template(
        'post/add-post.html', post=post, post_type=tag.post_type,
        path=[
            ('/post/{}'.format(tag.post_type), tag.post_type),
            ('#', 'Edit Post')
        ],
        curr_tab='Forum'
    )


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
