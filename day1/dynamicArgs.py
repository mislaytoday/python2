# coding:utf-8
# dynamic args use * 
# *args 是可变参数，args接收的是一个tuple
def calc(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum
  
print '10 * 8',calc(10,8)
print '10 * 8 * 5',calc(10,8,5)
nums = [2,3,4]
print 'nums =',nums
print 'nums calc =',calc(*nums)