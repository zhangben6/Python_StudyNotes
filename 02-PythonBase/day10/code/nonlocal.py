# nonlocal.py

# 此示例示意nolocal 语句的语法和用法
v = 100
def f1():
    v = 200
    print("f1.v=", v)
    def f2():
        nonlocal v
        v = 300
        print("f2.v=", v)
    f2()
    print("f1.v=", v)
f1()
print("全局的v=", v)