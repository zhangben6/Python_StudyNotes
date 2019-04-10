# nonlocal2.py

# 3. 当有两层或两层以上函数嵌套时,访问nonlocal变量
# 只对最近的一层变量进行操作
v = 100
def f1():
    v = 200
    print("f1.v=", v)
    def f2():
        v = 300
        def f3():
            nonlocal v
            v = 400
        f3()
        print("f2.v=", v)
    f2()
    print("f1.v=", v)
f1()
print("全局的v=", v)