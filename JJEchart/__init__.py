# -*- coding: utf-8 -*-

from flask import Flask
from flask_moment import Moment
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_bootstrap import Bootstrap

app = Flask('JJEchart')
app.config.from_pyfile('config.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

#db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
Session = sessionmaker()

# from JJEchart import views, errors, commands
from JJEchart import errors,views