def mydeco(fn):
    return fn

@mydeco
def fun():
    print("fun函数被调用")

# fun = mydeco(fun)
fun()  # 调用原来的