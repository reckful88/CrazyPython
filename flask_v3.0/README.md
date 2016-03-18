我们将把应用的包存放在这个app文件夹下。这个静态子文件件夹我们用来放诸如图片、JS或者CSS之类的文件，而template子文件夹则明显用于存放template文件的。

microblog
    |-flask文件夹
    |-<一些虚拟环境的文件>
    |-app文件夹
    |  |-static文件夹
    |  |-templates文件夹
    |  |-__init__.py文件
    |  |-views.py文件
    |-tmp文件夹
    |-run.py文件



模板继承:extends 语句


库：
Flask-WTF是WTForms项目的Flask框架扩展，我们将用他来帮助我们处理web表单





views:
'''这个视图非常的简单，它仅仅就是返回一个string语句，显示在用户的web浏览器上。
功能上的两条路径连接这从urls/and/index到这个功能的映射。'''

'''因为我们这个小程序还支持用户功能，所以咱用了一个用户占位对象，
通常它被亲切的称呼为假数据或测试数据。它可以让我们关注程序中急需解决的部分。'''

'''从 Flask 框架 import 了一个叫 render_template 的新函数，并用这个函数来渲染模板。
并给这个函数赋予了模板文件名和一些变量作为参数。
它将导入的变量替换掉模板中的变量占位符，并返回渲染后的模板。'''

'''在 Flask 底层，render_template 函数实际上是调用了 Flask 的一个组件： Jinja2 模板处理引擎。
是 Jinjia2 用导入的变量替换掉了模板中对应的 {{ ... }} 代码块。'''

在提交请求时调用了表单的 validate_on_submit() 方法后，它会从请求中获取所有提交的数据，
然后使用表单字段中绑定的验证函数进行数据验证。在所有的数据都验证通过时会返回 True.
这就意味着你可以放心的使用这些表单数据了。
只要有一个字段验证不通过，它都会返回 False. 这时就需要我们返回数据给用户
当 validate_on_submit() 方法返回 True 的时候，我们的视图函数又会调用两个新的函数。
它们都是从Flask 中引入的，flash 函数用来在下一个打开的页面中显示定义的消息。

将把已经登录的用户放到g变量里

oid.try_login是通过Flask-OpenID来执行用户认证。

基于OpenID的认证是异步的。如果认证成功，Flask-OpenID将调用有由oid.after_login装饰器注册的方法。
如果认证失败那么用户会被重定向到login页面。



init:
登录系统,我们将使用两个扩展,Flask-Login 和 Flask-OpenID
在没有邮件服务器的pc上测试邮件功能,打开一个控制台窗口，并且运行下面的命令：
python -m smtpd -n -c DebuggingServer localhost:25






index:
用数组存储用户的文章，每一个数组元素都是一个字典，
如上代码所示，这个dict的key是author和body，用来存储文章的作者和文章内容
继承于刚刚添加的基础模板 base.html



form：
使用 OpenId 登录只需要一个字符串，然后发送给 OpenId 服务器就行了。
另外我们还需要在表单中加一个“记住我” 的选项框，这个是送给那些不想每次来我们网站都要进行身份认证的人。
选择这个选项后，首次登录时会用cookie在他们的浏览器上记住他们的登录信息，
下次再进入网站时就不需要进行登录操作。



base：
添加一个导航菜单，里面包含 修改个人资料，退出登录 等类似的链接


login.html:
表单模版



OpenId:
现实生活中，我们发现有很多人都不知道他们拥有一些公共账号。
一部分大牌的网站或服务商都会为他们的会员提供公共账号的认证。
举个栗子，如果你有一个 google 账号，其实你就有了一个公共账号，类似的还有 Yahoo, AOL, Flickr 等。
为了方便我们的用户能简单的使用他们的公共账号，我们将把这些公共账号的链接添加到一个列表，
这样用户就不用自手工输入了。



SQLAlchemy:
已封装了关系对象映射（ORM）的一个插件
sqlite是小程序数据库的最佳选择，一个可以以单文件存储的数据库。
SQLAlchemy-migrate包自带命令行工具和APIs来创建数据库，这样的方式可以方便以后更新

DB:
脚本创建数据库
执行完db_migrate.py 将打印出Current database version: 1
数据库升级、回滚
执行db_migrate.py 将得到Current database version: 2

'''
这样我们的数据库模块和models就被加载到了内存里.
>>> from app import db, models

让我们来创建个新用户：
>>> u = models.User(nickname='john', email='john@email.com')
>>> db.session.add(u)
>>> db.session.commit()
>>>

让我们来添加另外一个用户：
>>> u = models.User(nickname='susan', email='susan@email.com')
>>> db.session.add(u)
>>> db.session.commit()
>>>

现在我们可以查询出用户信息：
>>> users = models.User.query.all()
>>> users
[<User u'john'>, <User u'susan'>]
>>> for u in users:
...     print(u.id,u.nickname)
...
1 john
2 susan
>>>

另外一种方式来查询，如果我们知道了用户的id，我们可以使用下面的方式查找用户信息：
>>> u = models.User.query.get(1)
>>> u
<User u'john'>
>>>

添加一条微博信息：
>>> import datetime
>>> u = models.User.query.get(1)
>>> p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
>>> db.session.add(p)
>>> db.session.commit()
'''
这个地方我们把时间设置为UTC时区，所有的存储在数据库里的时间将是UTC格式，用户可能在世界各地写微博，因此我们需要使用统一的时间单位。在以后的教程中我们将学习如何在用户本地时区使用这些时间。
你也许注意到我们没有在Post类中设置user_id字段，取而代之的是把用户对象存储到了author字段。auhtor字段是个通过Flask-SQLAlchemy添加的虚拟字段用来建立关联关系的，我们之前已经定义好了这个名字，参照：model中的db.relationship中backref参数。通过这些信息，ORM层就能知道如何取到user_id。
要完成这个会话，让我们来看看更多可做的数据库查询：
# get all posts from a user
>>> u = models.User.query.get(1)
>>> u
<User u'john'>
>>> posts = u.posts.all()
>>> posts
[<Post u'my first post!'>]

# obtain author of each post
>>> for p in posts:
...     print(p.id,p.author.nickname,p.body)
...
1 john my first post!

# a user that has no posts
>>> u = models.User.query.get(2)
>>> u
<User u'susan'>
>>> u.posts.all()
[]

# get all users in reverse alphabetical order
>>> models.User.query.order_by('nickname desc').all()
[<User u'susan'>, <User u'john'>]
>>>

在结束会话之前，我们把之前创建的测试用户和文章删除掉，就可以在接下来的章节，从一个干净的数据库开始：
>>> users = models.User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = models.Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()
>>>
