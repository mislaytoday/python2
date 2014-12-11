# coding:utf-8
def f(x):
  return x*x
''' 对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返'''
m = map(f,[1,2,3,4,5,6,7,8,9])
print m
