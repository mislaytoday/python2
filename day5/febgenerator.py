# coding=utf-8
'''
打印斐波拉契数列
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
a=b, b=a+b
'''
listfib = []
def fib(max):
  n,a,b = 0,0,1
  while n < max:
    listfib.append(b)
    print b
    a,b = b , a+b # a = b , b = a + b
    n = n + 1
fib(8)
print 'listfib', listfib
'''
把fib函数变成generator
'''
def fib2(max):
  n,a,b = 0,0,1
  while n < max:
    yield b
    a,b = b , a+b # a = b , b = a + b
    n = n + 1
for x in fib2(8):
  print x