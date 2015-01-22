# coding=utf-8
import functools;
max2 = functools.partial(max,10)
print max2(5,6,7)
int2 = functools.partial(int,base = 2)
print int2('1010101101101101001')