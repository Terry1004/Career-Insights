from flask import (
    Blueprint, redirect, render_template, request, flash, session, url_for
)
from ..models.post import Post


bluePrint = Blueprint('search', __name__, url_prefix='/search')


@bluePrint.route('', methods=['GET','POST'])
def detail():
    if request.method == 'GET':
        return render_template('search/search.html')

    if request.method == 'POST':
        uni = request.form['uni']
        name = request.form['name']
        company = request.form['company']
        keywords = request.form['keywords']
        title = request.form['title']

        print(uni)
        print(type(name))
        print(type(company))

        if company == '':
            print("yes")

        posts = []
        if company != '':
            post1 = Post.find_by_company(company)
            if post1:
                posts.extend(post1)
        if name != '':
            post2 = Post.find_by_name(name)
            if post2:
                posts.extend(post2)
        if uni != '':
            post3 = Post.find_by_uni(uni)
            if post3:
                posts.extend(post3)
        if title != '':
            post4 = Post.find_by_title(title)
            if post4:
                posts.extend(post4)
        if keywords != '':
            post5 = Post.find_by_keywords(keywords)
            if post5:
                posts.extend(post5)

        if posts:
            return render_template('post/index.html', posts=posts)
        else:
            return render_template('error/404.html', message='No Posts Found relevant to search')
