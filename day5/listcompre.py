# coding=utf-8
a = [1,2,3,4,5,6,7,8,9]
b = [x * x for x in a]
c = [x * x for x in a if x%2 ==0]
print 'list a = ',a
print 'list 1*1,2*2,3*3,4*4',b
print 'if x%2=0 x*x',c
a = ['Admin','Lower','Sayid',123]
e = [x.lower() for x in a if isinstance(x,str)]
print 'a = ',a
