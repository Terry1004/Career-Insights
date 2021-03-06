from flask import (
    Blueprint, redirect, render_template,
    request, flash, session, url_for, abort
)
from ..models.comment import Comment
from .auth import login_required


blueprint = Blueprint('comment', __name__, url_prefix='/comment')


@blueprint.route('/add-comment', methods=['POST'])
@login_required
def add_comment():
    uni = session['uni']
    post_id = request.form['post_id']
    content = request.form['content'].strip()
    comment_id = request.form.get('comment_id', None)
    error = False
    if not content:
        flash('Content is required.')
        error = True
    if error:
        return redirect(url_for('post.detail', post_id=post_id))
    else:
        reply_id = Comment.get_max_id(post_id) + 1
        comment = Comment(post_id, reply_id, uni, content)
        comment.save(comment_id=comment_id)
        return redirect(url_for('post.detail', post_id=post_id))


@blueprint.route('/edit-comment', methods=['POST'])
@login_required
def edit_comment():
    post_id = request.form['post_id']
    comment_id = request.form['comment_id']
    comment = Comment.find_by_id(post_id, comment_id)
    if comment.uni != session['uni']:
        abort(403)
    content = request.form['content']
    comment.content = content
    comment.save(update=True)
    return redirect(url_for('post.detail', post_id=post_id))


@blueprint.route('/delete-comment', methods=['POST'])
@login_required
def delete_comment():
    post_id = request.form['post_id']
    comment_id = request.form['comment_id']
    comment = Comment.find_by_id(post_id, comment_id)
    if comment.uni != session['uni']:
        abort(403)
    comment.destroy()
    return redirect(url_for('post.detail', post_id=post_id))
