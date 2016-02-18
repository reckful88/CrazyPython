#!/usr/bin/env python
#-*- coding: utf-8 -*-

#multiprocessing.py

import os
print 'Process (%s) start...' % os.getpid()
pid = os.fork()
print pid
if pid == 0:
    print 'child process (%s) and my parent is %s.' % (os.getpid(), os.getpid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(),pid)

print 'hello'
