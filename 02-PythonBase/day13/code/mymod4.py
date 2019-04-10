# mymod4.py

# 此示例示意模块的隐藏属性

def f1():
    _f2()
    __f3()
    __f4__()

def _f2():
    pass

def __f3():
    pass

def __f4__():
    pass

name1 = "aaaa"
_name1 = 'bbbb'

