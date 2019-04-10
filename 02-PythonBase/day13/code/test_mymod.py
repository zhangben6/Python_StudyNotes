# file : test_mymod.py

# 此程序将作为主模块来调用mymod.py里的函数和数据
import mymod
# import copy
# import pdb
import os

mymod.myfac(5)
mymod.mysum(100)

print(mymod.name1)
print(mymod.name2)

from mymod import name1
print(name1)  # Audi

from mymod import *
mysum(9999)
myfac(8888)
print(name2)
