#-*- coding:utf-8 -*-

#用户登录表单
#
'''我们引入了一个 Form 类，然后继承这个类，按需求还添加了 TextField 和 BooleanField 这两个字段。
另外还引入了一个表单验证函数 Required，
这种验证函数可以附加在字段里面，在用户提交表单时它们会用来检查用户填写的数据。
这个 Required 函数是用来防止用户提交空数据'''


from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])