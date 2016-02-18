#!/usr/bin/env python
#-*- coding:utf-8 -*-

class queue(object):
    def __init__(self):
        self.mylist = []
    def pop(self):
        return self.mylist.pop(0)
    def push(self,x):
        return self.mylist.append(x)
    def isempty(self):
        if len(self.mylist):
            return None
    def top(self):
        if self.isempty():
            return None
        return self.mylist
q = queue()
q.isempty() == True
q.push('a')
q.isempty() == False
q.top()
q.pop()
q.isempty
