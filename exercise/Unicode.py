#!/usr/bin/env python
# =*= coding: utf-8 -*-

'''
熟悉了解Unicode 和 格式化
'''

print ord('A')
print chr(65)

print u'中文'
print u'中'

print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')

print len (u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x97')

print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')


print 'Hello,%s' % 'world'
print 'Hi, %s, you have $%d.' % ('Michael',100000)
print 'nihao, %s, ni you %d yuan' % ('sam',100)
print 'nihao, %s, ni you %f yuan, ni de nian ling shi %d sui' % ('Jack',15,22)


