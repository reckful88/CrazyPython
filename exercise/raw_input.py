#!/usr/bin/env python
#-*- coding:utf-8 -*-

birth = raw_input('birth:')
if birth < 2000:
    print '00前'
else:
    print '00后'
'''输入1982，结果却显示00后，原因如下：'''
print birth
print '1982' < 2000
print 1982 < 2000

'''因为从raw_input() 读取的内容永远以字符串的形式返回，把字符串和整数比较就不会
得到期待的结果，必需先用int()把字符串转换成为我们想要的整形：
birth = int(raw_input('birth:'))
'''

