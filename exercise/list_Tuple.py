#!/usr/bin/env python
# -*- coding: utf-8 -*-


classmates = ['Michael','Bob','Tracy']
print classmates

'''
len() 函数可以获得list元素的个数
用索引访问list中的每一个位置的元素，索引是从0开始
'''
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
#如果 print classmates[3] 会报indexError错误，因为超出了范围，这里目前只有3个元
#素，从0开始 是第一个元素

'''
-1做索引 直接获取最后一个元素，就是倒数
'''
print classmates[-1]
print classmates[-2]
print classmates[-3]
#这里也一样，如果classmates[-4]将会超出范围

'''
list是一个可变的有序表，可以往list中追加元素到末尾
'''
classmates.append('Adam')
print classmates

'''
也可以把元素插入到指定的位置，比如索引号为1的位置
'''
classmates.insert(1,'Jack')
print classmates

'''
要删除list末尾的元素，用pop()方法
'''
classmates.pop()
print classmates

'''
要删除指定位置的元素，用pop(i)方法，其中i是索引位置
'''
classmates.pop(1)
print classmates

'''
要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
'''
classmates[1] = 'Sarah'
print classmates

'''
list里面的元素的数据类型也可以不相同，比如：
'''
L = ['Apple',123,True]

'''
list元素也可以是另一个list，比如
'''
s = ['python','java',['asp','php'],'scheme']
print len(s)

p = ['asp','php']
s = ['python','java',p,'scheme']      #要拿到'asp'可以写p[0]或者s[2][0]

'''
如果一个list中一个元素也米有，就是一个空的list，它的长度为0
'''
L = []
print len(L)

'''
另一种有序列表叫元祖:tuple
tuple和list非常相似，但是tuple一旦初始化就不能修改
'''

classmates = ('Michael','Bob','Tracy')   #现在classmates这个tuple不能变了，
#它没有append().insert()这样的用法，但获取元素的方法是一样的，如
#classmates[0],classmates[-1]， 但不能赋值称另外的元素

t = (1,2)
print t
print type(t)

'''
定义的不是tuple，是1这个数字！这是因为括号()既可以表示tuple，又可以表示数学公式
中的小括号，这就产生了歧义，所以只有1个元素的tuple定义时必需加一个逗号,
来消除歧义
'''

t = (1)
print t
print type(t)

t = (1,)
print t
print type(t)


'''
python在显示只有1个元素的tuple时，也会加一个逗号，
以免你误解成数学计算意义上的括号
最后来看一个“可变的”tuple
'''
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t         


'''
小结：list和tuple是python内置的有序集合，一个可变，一个不可变。
根据需求来选择使用它们。
'''






















