#-*- coding: utf-8 -*=

'''
Return the absolute value of a number. The argument may be a plain or long
integer or a floating point number. If the argument is a complex number, its
magnitude is returned.

返回一个数的绝对值。参数可以是一个平原或长整数或浮点数。如果参数是一个复数,返回
它的大小。
'''

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


print all('element')
print all('')


