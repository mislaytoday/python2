# coding=utf-8
def abc(a,b,c):
  return a*10000 + b*100 + c
list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]
''' 如果给出了额外的可迭代参数，则对每个可迭代参数中的元素
    '并行’的应用‘functi'  '''
m = map(abc,list1,list2,list3)
print m
