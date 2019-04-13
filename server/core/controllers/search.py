from flask import (
    Blueprint, redirect, render_template,
    request, flash, session, url_for, abort
)
from ..models.post import Post


blueprint = Blueprint('search', __name__, url_prefix='/search')


@blueprint.route('', methods=['GET', 'POST'])
def detail():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        title = request.form['title']
        posts1, posts2, posts3 = [], [], []
        if name:
            posts1 = Post.find_by_name(name)
        if company:
            posts2 = Post.find_by_company(company)
        if title:
            posts3 = Post.find_by_title(title)
        return render_template(
            'post/index.html',
            posts=posts1 + posts2 + posts3
        )
    return render_template('search/search.html')
