#! /usr/bin/env python
# -*- coding: utf-8 -*-

a = 1

name = 'tom'

def func():
    a = 2
    global name
    name = 'jerry'
#    print(f"a = {a}")
    print(f"func {name}")
#print(a)

print(name)
func()
print('调用函数之后的name')
print(name)

