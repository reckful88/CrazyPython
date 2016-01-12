#!/usr/bin/env  python
#-*- coding:utf-8 -*-

#判断

'''elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''

age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

'''if语句执行有个特点，它是从上往下判断，如果在某个判断上是true，就把该判断对应
的语句执行后，就忽略掉剩下的elif和else'''
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

'''if判断条件还可以简写，比如写：
if x:
    print 'True'
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False'''


#循环
'''python的循环有两种，一种是for..in循环，依次把list或tuple中的每个元素迭代出来
，看例子：'''

names = ['Michael','Bob','Tracy']
for name in names:
    print name
#所以for x in 循环就是把每个元素代入变量x，然后执行缩进块的语句。

'''计算1-10的整数和'''
sums = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sums = sums + x
print sums

'''计算1-100的乘积'''
nums = 1
for x in range(1,101):
    nums = nums * x
print nums


'''while循环,只要条件满足，就不断循环，条件不满足时退出循环'''
'''计算100以内的所有奇数之和'''
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print sum














