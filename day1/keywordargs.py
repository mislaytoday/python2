# coding:utf-8
# **kw 是关键字参数，kw接收的是一个dict
def person(name,age,**kw):
  print 'name:',name,'age:',age,'other',kw
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack2', 24, **kw)