# function_variable.py

def f1():
    print("f1函数被调用!")

def f2():
    print("f2函数被调用!")

f1, f2 = f2, f1  # 交换两个函数名变量的绑定关系

f1()  # 请问调用谁?