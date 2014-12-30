# coding=utf-8
dict = {'a':1,'b':2,'c':3}
print 'dict = ',dict
# 迭代Key
for key in dict:
  print 'dict key=',key
  print 'dict value=',dict[key]

# 迭代Value
for value in dict.itervalues():
  print value
 
# 同时迭代Key和Value
for k,v in dict.iteritems():
  print k,v