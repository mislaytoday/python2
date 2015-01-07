# coding=utf-8
def getlist(max):
  list = []
  n,a,b = 0,0,1
  while (n <=max):
    list.append(b)
    a,b = b,a+b
    n = n + 1
  return list
print getlist(10)