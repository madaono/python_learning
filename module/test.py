#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello,%s!' % args[1])
    else:
        print('too many arguments')

if __name__ == '__main__':
    test()


# 前两行是表示这个PY可以直接在unix/linux/mac上运行，第二行代表使用UTF编码

# 类型JS的作用域，如果模块中需要隐藏函数则

def _private_1(name):
    return 'Hello,%s' % name
def _private_2(name):
    return 'Hi,%s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)