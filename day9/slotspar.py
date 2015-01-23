# coding = utf-8
class Student(object):
  __slots__=('name','age')
class GraduateStudent(Student):
  __slots__=('score')
g = GraduateStudent()
g.name = 'sayid'
g.age = 20
g.score = 9999
print 'name = %s,age = %s,score = %s'%(g.name,g.age,g.score)