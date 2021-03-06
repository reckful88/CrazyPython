#-*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


'''这是Flask-WTF需要用到的2个配置项。CSRF_ENABLED配置启用了跨站请求攻击保护，
大部分情况下你都需要开启此功能，这能使你的应用更安全。'''


#处理 OpenID 登录
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


# 数据库文件的路径。
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
# 存储SQLAlchemy-migrate数据库文件的文件夹
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# 配置Flask-WhooshAlchemy
WHOOSH_BASE = os.path.join(basedir, 'search.db')


#通过email发送错误日志
# mail server settings
MAIL_SERVER = 'your.mailserver.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['you@example.com']


# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50


# email server
#MAIL_SERVER = 'smtp.googlemail.com'
#MAIL_PORT = 465
#MAIL_USE_TLS = False
#MAIL_USE_SSL = True
#MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
#ADMINS = ['your-gmail-username@gmail.com']
