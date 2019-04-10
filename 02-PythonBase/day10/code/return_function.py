# return_function.py


def f1():
    print("我是f1函数")

def f2():
    print("我是f2函数")

def get_fx(n):
    if n == 1:
        return f1
    elif n == 2:
        return f2
# 此时fx就是函数f1
fx = get_fx(1)
fx()  # 调用f1


fx = get_fx(2)
fx()  # 请问调用谁?