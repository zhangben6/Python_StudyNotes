# mymod3.py

# 此示例示意用__all__列表限制 用from import *导入
# 相应的属性

__all__ = ['f1', 'name1']

def f1():
    f2()
    f3()

def f2():
    pass

def f3():
    pass

name1 = 'aaaaa'
name2 = 'bbbbb'

