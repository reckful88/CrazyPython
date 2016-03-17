#-*- coding:utf-8 -*-
#/usr/bin/env python

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))




'''这个是创建数据库脚本，
./db_create.py   执行
运行这条命令之后，你就创建了一个新的app.db文件。这是个支持迁移的空sqlite数据库，
同时也会生成一个带有几个文件的db_repository目录，这是SQLAlchemy-migrate存储数据库文件的地方，
注意如果数据库已存在它就不会再重新生成了。这将帮助我们在丢失了现有的数据库后，再次自动创建出来。'''
