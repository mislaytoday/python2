# coding=utf-8
dict = {'a':1,'b':2,'c':3}
print 'dict = ',dict
# ����Key
for key in dict:
  print 'dict key=',key
  print 'dict value=',dict[key]

# ����Value
for value in dict.itervalues():
  print value
 
# ͬʱ����Key��Value
for k,v in dict.iteritems():
  print k,v