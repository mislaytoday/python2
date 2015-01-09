#coding=utf-8
def funcxx(args):
  return args*args
def funcxxx(x,y):
  return x*y
lista = [1,2,3,4,5,6,7,8,9]
'''
map()函数接收两个参数，一个是函数，一个是序列,
map将传入的函数依次作用到序列的每个元素，
并把结果作为新的list返回。
'''
mapa = map(funcxx,lista)
maps = map(str,lista)
'''
reduce把一个函数作用在一个序列[x1, x2, x3...]上，
这个函数必须接收两个参数，reduce把结果继续和序列
的下一个元素做累积计算
'''
reducea = reduce(funcxxx,lista)
print 'lista = [1,2,3,4,5,6,7,8,9]'
print 'mapa = map(funcxx,lista)'
print mapa
print 'maps = map(str,lista)'
print maps
print 'reducea = reduce(funcxxx,lista)'
print reducea