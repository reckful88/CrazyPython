#-*- coding:utf-8 -*-
#/usr/bin/env python

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from datetime import datetime
from app import app, db, lm, oid
from .forms import LoginForm, EditForm
from .models import User



# index view function suppressed for brevity

#从数据库加载到一个用户
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
#记住Flask-Login里的user id一直是unicode类型的，所以在我们把id传递给Flask-SQLAlchemy时，有必要把它转化成integer类型。
#

#任何一个被before_request装饰器装饰的方法将会在每次request请求被收到时提前与view方法执行
@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required   #表明了这个页面只有登录用户才能访问
def index():
    user = g.user   #把g.user传给了模板，替换了之间的假对象。
    posts = [ #fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'boddy': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)


#渲染登录表单对象到模板的视图函数
#从表单中接收数据
'''validate_on_submit() 这个方法做了表单处理的所有工作。
如果你在表单向用户提供数据时(举个栗子：用户在它之前修改了一下提交的数据) 时调用此方法，它会返回 False。
'''



'''在方法体的开头，我们检测是是否用户是已经经过登录认证的，如果是就重定向到index页面。
这儿的思路是如果一个用户已经登录了，那么我们不会让它做二次登录。'''
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler #新的装饰器：oid.loginhandler。它告诉Flask-OpenID这是我们的登录视图函数。
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(usr_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])


#Flask-OpenID登录回调
@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":   #为了验证，要求一个有效的email
        flash('Invalid login. please try agagin.')
        return redirect(usr_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember= remember_me) #根据email查找数据库。如果email没有被找到我们就认为这是一个新的用户
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                            user = user,
                            posts =  posts)


@app.route('/edit', methods = ['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(user_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)
