#coding=utf-8
'''
filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):
  return n % 2 == 1 # 返回奇数
print filter(is_odd,[1,2,4,5,6,9,10,15,20])

def not_empty(s):
  return s and s.strip() # s.strip(rm),删除字符序列,当rm为空时,默认删除空白符(包括'\n', '\r',  '\t',  ' ')
listTest = ['A','B','',None,'D']
print filter(not_empty,listTest)

def test_return(s):
  return s and s.strip()
list_return = []
list_return.append(test_return(' AA'))
print list_return
list_return.append(test_return(''))
print list_return