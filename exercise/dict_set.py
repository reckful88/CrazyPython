#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''需要牢记的是 dict的key 必须是不可变对象！！
在python中字符串、整数都是不可变的，因此可以放心地作为key。
而list是可变的，就不能作为key'''


'''python中内置了字典：dict的支持，dict全称dictionary，在其它语言中也称为map，
使用键－值（key-value）存储，具有极快速的查找速度。'''

d = {'Michael':95,'Bob':75,'Tracy':85}
print d
print d['Michael']

d['Adam'] = 67   #可以添加新的kv，如果已经存在的，将会把存在的冲掉
print d['Adam']
print d    
d['Jack'] = 90
print d['Jack']
d['Jack'] = 88
print d['Jack']

'''如果key不存在，dict就会报错：
>>> d['Thomas']
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
KeyError: 'Thomas'
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
>>> 'Thomas' in d
False
二是通过dict提供的get方法，如果key不存在，可以返回none，或者自己指定的value：
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
注意：返回none的时候python的交互式命令行不显示结果。'''

'''要删除一个key，用pop(key)方法，对应的value也会从dict中删除:'''
d.pop('bob')
print d
#请注意，dict内部存放的顺序和key放入的顺序是没有关系的。


'''set'''
'''set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以在set中
，没有重复的key。要创建一个set，需要提供一个list作为输入集合：'''

s = set([1,2,3])
print s
print type(s)
'''重复元素在set中自动被过滤:'''
s = set([1,1,2,2,3,3,3])
print s

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print s
s.add(4)
print s






















