# -*- coding:utf-8 -*-
class Student(object):
  def __init__(self,name,score):
    self.name = name
    self.score = score
  def print_score(self):
    print '%s: %s'%(self.name,self.score)

micky = Student('micky',56)
lili = Student('lili',80)
micky.print_score()
lili.print_score()