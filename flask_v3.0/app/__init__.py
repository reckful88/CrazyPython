#-*- coding:utf-8 -*-
#/usr/bin/env python

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))
#Flask-OpenID 扩展为了可以存储临时文件，需要一个临时文件夹路径。为此,我们提供了它的位置


from app import views, models
