# global.py


# 4. global变量列表里的变量名不能出现在函数的形参列
#        表里

v = 100
def f1(v):
    global v  # 此处出错
    v = 200

f1(300)
