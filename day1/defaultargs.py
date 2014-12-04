# coding:utf-8
# notice: 
# 必选参数在前,默认参数在后
def power(x,n=2):
  s = 1
  while n > 0:
    n = n -1
    s = s * x
  return s

print 'power (5,2)=',power(5,2)
print 'power (5)=',power(5)
print 'power (5,10)=',power(5,10)