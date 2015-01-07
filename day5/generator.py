# coding=utf-8
a = (1,2,3,4,5,6,7,8,9)
b = (x * x for x in a)
c = (x * x for x in a if x%2 ==0)
print 'list a = ',a
print 'list 1*1,2*2,3*3,4*4'
for n in b:
  print n
print 'if x%2=0 x*x'
for n in c:
  print n
a = ('Admin','Lower','Sayid',123)
e = (x.lower() for x in a if isinstance(x,str))
print 'a = '
for n in e:
  print n