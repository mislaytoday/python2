# coding=utf-8
class Fib(object):
  def __init__(self,value):
    self.a,self.b,self.max_value = 0,1,value
  def __iter__(self):
    return self
  def next(self):
    self.a, self.b = self.b, self.a+self.b
    if self.a > self.max_value:
      raise StopIteration();
    return self.a
  def __str__(self): # 重写该类的print
    return 'Here is Fib class'
  __repr__ = __str__

a = Fib(1000)
print a
for n in a:
  print n