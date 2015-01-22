#!/usr/bin/env python
#-*- coding: utf-8 -*-
'a test hello module'
__author__ = 'Sayid Locke'
import sys
def test():
  args = sys.argv
  module_name = sys.copyright
  if len(args) == 1:
    print 'builtin_module_names = %' %module_name
    print 'Hello World! sys.argv = %s'%args
  elif len(args) == 2:
    print 'Hello,%s!'%args[1]
  else:
    print 'Too many arguments!'

if __name__ =='__main__':
  test()