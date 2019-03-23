import os
from flask import Flask, render_template
from sqlalchemy import create_engine

from utils.database import get_db_url
from core.controllers import auth, profile


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.database = create_engine(get_db_url(app.config))
app.register_blueprint(auth.blueprint)
app.register_blueprint(profile.blueprint)


@app.route('/')
def index():
    return render_template('index.html')
