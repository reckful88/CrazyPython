#-*- coding:utf-8 -*-

'''User表结构：
            Users
id           Integer
nickname     varchar(64)
email        varchar(120)
role         Integer
'''


'''User类把我们刚刚创建的几个字段定义为类变量。字段使用db.Column类创建实例，字段的类型作为参数，
另外还提供一些其他可选参数。例如，标识字段唯一性和索引的参数.
__repr__方法告诉Python如何打印class对象，方便我们调试使用。'''

from app import db

#ROLE_USER = 0
#ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)



#通常这个方法应该返回True，除非对象代表一个由于某种原因没有被认证的用户。
    @property
    def is_authenticated(self):
        return True


#为用户返回True除非用户不是激活的，例如，他们已经被禁了
    @property
    def is_active(self):
        return True


#为那些不被获准登录的用户返回True
    @property
    def is_anonymous(self):
        return False


#为那些不被获准登录的用户返回True
    def get_id(self):
        try:
            return unicode(self.id) #python2
        except NameError:
            return str(self.id) #python3


    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % \
            (md5(self.email.encode('utf-8')).hexdigest(), size)


    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

'''增加了一个表示用户写的微博的Post类，user_id字段在Post类中被初始化指定为一个外键，
因此Flask-SQLAlchemy会知道这个字段将会和用户做关联。'''
