# coding=utf-8
x = abs(-10)
print "x = abs(-10), x=" ,x
x = abs
print "x = abs, x=" ,x

'''
一个函数接收另一个函数作为参数,
这种函数就称之为高阶函数
'''
def add(x,y,f):
  return f(x) + f(y)
y = add(-5,6,abs)
print y
