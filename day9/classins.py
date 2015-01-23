# coding = utf-8 
class Animal(object):
  pass
class Dog(Animal):
  pass
class Husky(Dog):
  pass
a = Animal()
d = Dog()
h = Husky()
print 'isinstance(h,Husky)', isinstance(h,Husky)
print 'isinstance(h,Dog)', isinstance(h,Dog)
print 'isinstance(h,Animal)', isinstance(h,Animal)
print 'isinstance(d,Husky)', isinstance(d,Husky)
dd = 'ABC'
print 'dir(\'Abc\')',dir(dd)
print dd.__len__()
print 'ABC'.__len__()