from flask import (
    Blueprint, redirect, render_template,
    request, flash, session, url_for, abort
)
from ..models.post import Post
from ..utils import non_empty_items


blueprint = Blueprint('search', __name__, url_prefix='/search')


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'search/index.html', path=[('/search', 'Search')], curr_tab='Search'
    )


@blueprint.route('/search-result', methods=['POST'])
def search():
    keywords = request.form['keywords'].strip().split()
    name = request.form['name'].strip()
    company = request.form['company'].strip()
    title = request.form['title'].strip()
    content = request.form['content'].strip()
    domain = request.form['domain'].strip()
    hashtags = request.form['hashtags'].strip().split(',')
    posts = None
    error = False
    if keywords:
        posts1 = set(Post.find_by_keywords(keywords))
        if posts is None:
            posts = posts1
        else:
            posts &= posts1
    if name:
        posts2 = set(Post.find_by_name(name))
        if posts is None:
            posts = posts2
        else:
            posts &= posts2
    if company:
        posts3 = set(Post.find_by_company(company))
        if posts is None:
            posts = posts3
        else:
            posts &= posts3
    if title:
        posts4 = set(Post.find_by_title(title))
        if posts is None:
            posts = posts4
        else:
            posts &= posts4
    if content:
        posts5 = set(Post.find_by_content(content))
        if posts is None:
            posts = posts5
        else:
            posts &= posts5
    if domain:
        posts6 = set(Post.find_by_domain(domain))
        if posts is None:
            posts = posts6
        else:
            posts &= posts6
    if non_empty_items(hashtags):
        posts7 = set(Post.find_by_hashtags(hashtags))
        if posts is None:
            posts = posts7
        else:
            posts &= posts7
    if posts is None:
        flash('At least one field has to be non-empty.')
        error = True
    if error:
        return redirect(url_for('search.index'))
    else:
        return render_template(
            'search/search-result.html', posts=posts,
            path=[('/search', 'Search'), ('#', 'Search Result')]
        )
