# coding=utf-8
'''
传入字符串,返回整形
'''
def strtoint(str):
  def fn(x,y):
    return x*10+y
  def strtonum(str):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]
  return reduce(fn,map(strtonum,str))
print strtoint('11111144442355')

'''

'''
def test(str):
  return {'0': '1', '1': '2'}[str]
print map(test,'0110')