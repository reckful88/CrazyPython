# -*- coding:utf-8 -*-
#all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect ,url_for, abort,\
render_template,flash

#创建一个实例
app = Flask(__name__)

#载入数据库实力文件夹
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'flaskr.db'),
    DEBUG = True,
    SECRET_KEY = 'development key',    #secret_key 是保证客户端会话的安全的要点
    USERNAME = 'root',
    PASSWORD = 'chrisk9999'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)  #导入配置


def connect_db():
    #创建一个简单的sql数据库链接
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

#初始化数据库
#应用对象的 open_resource() 方法是一个很方便的辅助函数，可以打开应用提供的资源
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

#调用函数，来创建数据库
#@app.cli.command('initdb')
#def initdb_command():
#    """Creates the database tables."""
#    init_db()
#    print ('Initialized the database.')

def get_db():
    #打开一个新的数据库连接
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    #再次关闭数据库的请求
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#显示条目
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

#@app.route('/')
#def show_entries():
#    cur = g.db.execute('select title, text from entries order by id desc')
#    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
#    return render_template('show_entries.html', entries=entries)

#添加条目
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))   #注意这里的用户登入检查（ logged_in 键在会话中存在，并且为 True
#安全提示 确保像上面例子中一样，使用问号标记来构建 SQL 语句。否则，当你使用格式化字符串构建 SQL 语句时，你的应用容易遭受 SQL 注入


#登入和登出
'''这些函数用来让用户登入登出。登入通过与配置文件中的数据比较检查用户名和密码，
并设定会话中的 logged_in 键值。如果用户成功登入，那么这个键值会被设为 True ，
并跳转回 show_entries 页。此外，会有消息闪现来提示用户登入成功。
如果发生一个错误，模板会通知，并提示重新登录。'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

#登出
'''登出函数，做相反的事情，从会话中删除 logged_in 键。
我们这里使用了一个简洁的方法：如果你使用字典的 pop() 方法并传入第二个参数（默认），
这个方法会从字典中删除这个键，如果这个键不存在则什么都不做。
这很有用，因为我们不需要检查用户是否已经登入。 '''

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
