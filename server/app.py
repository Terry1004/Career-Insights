import os
from flask import Flask, render_template, redirect, url_for
from sqlalchemy import create_engine

from utils.database import get_db_url
from core.controllers import auth, profile, post, search


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.database = create_engine(get_db_url(app.config))
app.register_blueprint(auth.blueprint)
app.register_blueprint(profile.blueprint)
app.register_blueprint(post.bluePrint)
app.register_blueprint(search.bluePrint)

@app.route('/')
def index():
    return redirect(url_for('post.index'))


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True, threaded=True)
