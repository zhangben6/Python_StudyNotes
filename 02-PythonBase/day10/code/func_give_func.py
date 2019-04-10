# func_give_func.py

def f1():
    print("f1函数被调用")

def f2():
    print("f2函数被调用")

def fx(fn):
    print("fn =", fn)
    fn()  # 调用fn绑定的函数

fx(f1)
# fx(f2)

print("程序结束")