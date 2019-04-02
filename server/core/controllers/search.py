from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.search import Search


bluePrint = Blueprint('post', __name__, url_prefix='/search')

@bluePrint.route('/search', methods=['GET'])
def detail():
    uni = request.args.get('uni')
    name = request.args.get('name')
    company = request.args.get('company')
    keywords = request.args.get('keywords')
    title = request.args.get('title')

    post1 = Search.find_by_company(company)
    post2 = Search.find_by_name(name)
    post3 = Search.find_from_posts(uni, title, keywords)

    # change this line to combine all posts and send
    if post1:
        return render_template('post/detail.html', post=post1)
    else:
        return render_template('error/404.html', message='Post Not Found.')
