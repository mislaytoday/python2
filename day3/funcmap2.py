# coding=utf-8
def abc(a,b,c):
  return a*10000 + b*100 + c
list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]
''' ��������˶���Ŀɵ������������ÿ���ɵ��������е�Ԫ��
    '���С���Ӧ�á�functi'  '''
m = map(abc,list1,list2,list3)
print m
