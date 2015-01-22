# coding=utf-8
class Student:
  def __init__(self,name,score):
    self.__name = name
    self.__score = score
  def get_score(self):
    print '%s : %s'%(self.__name,self.__score)
  def get_name(self):
    print self.__name
  def set_name(self,name):
    self.__name = name

lili = Student('lili',89)
lili.get_score()
lili.get_name()
lili.set_name('haha')
lili.get_score()
