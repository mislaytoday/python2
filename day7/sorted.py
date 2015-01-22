# coding=utf-8
'''
排序常规
对于两个元素x,和y,如果x<y则返回-1
如果x=y,则返回0
如果x>y,则返回1
'''
list_num = [36, 5, 12, 9, 21]
print 'num = [36, 5, 12, 9, 21]'
print 'sorted(num)',sorted(list_num)
list_str = ['bob', 'about', 'Zoo', 'Credit']
print 'list_str = [\'bob\', \'about\', \'Zoo\', \'Credit\']'
print 'sorted(list_str)',sorted(list_str)
def cmp_ignore_case(s1,s2):
  u1 = s1.upper()
  u2 = s2.upper()
  if (u1 < u2):
    return -1
  if (u1 > u2):
    return 1
  return 0
print 'sorted(list_str,cmp_ignore_case)',sorted(list_str,cmp_ignore_case)