#-*- coding:utf-8 -*-
#/usr/bin/env python

from app import app
app.run(debug = True)

'''这段脚本只是从我们的app包中导入了app的变量，然后调用它的方法来启动服务器。
记住，这个变量保存着我们上面创建的Flask实例'''
