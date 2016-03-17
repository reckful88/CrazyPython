#-*- coding:utf-8 -*-
#/usr/bin/env python
'''当你运行此脚本时，数据库将升级到最新版本，并通过脚本将改变信息存储到数据库中。'''

#数据库升级
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print ('Current database version: ' + str(v))
