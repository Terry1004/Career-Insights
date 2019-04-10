from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.post import Post


bluePrint = Blueprint('search', __name__, url_prefix='/search')


@bluePrint.route('/', methods=['GET','POST'])
def detail():
    if request.method == 'GET':
        return render_template('search/search.html')

    if request.method == 'POST':
        uni = request.args.get('uni')
        name = request.args.get('name')
        company = request.args.get('company')
        keywords = request.args.get('keywords')
        title = request.args.get('title')

        post1 = Post.find_by_company(company)
        post2 = Post.find_by_name(name)
        post3 = Post.find_from_posts(uni, title, keywords)
        all_posts = post1+post2+post3

        if all_posts:
            return render_template('post/index.html', post=all_posts)
        else:
            return render_template('error/404.html', message='No Posts Found relevant to search')
