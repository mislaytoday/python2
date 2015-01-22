# coding=utf-8
import functools

def log(func):
  def wrapper(*args,**kw):
    print 'call %s():' %func.__name__
    return func(*args,**kw)
  return wrapper

@log
def now():
  print '2015-01-21'

f=now
f()
print now.__name__

def logtext(text):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      print '%s %s():' %(text,func.__name__)
      return func(*args,**kw)
    return wrapper
  return decorator
@logtext('execute')

def nownow():
  print 'now now 2015-01-21'

nownow()
print nownow.__name__

def logall(text = 'default'):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      print 'start %s %s'%(text,func.__name__)
      func(*args,**kw)
      print 'end %s %s'%(text,func.__name__)
    return wrapper
  return decorator
@logall()
def nownownow():
  print ' 2015-01-21 '
@logall('hahaha')
def nownowhaha():
  print ' 2015-01-21'
nownownow()
nownowhaha()