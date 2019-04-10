# namespace.py

python的作用域
  作用域也叫名字空间，是访问变量时查找变量的名范围空间

python中的四个作用域 LEGB
   作用域             英文解释          英文缩写
局部作用域          Local(function)          L
外部嵌套函数作用域  Enclosing Fucntion local  E
函数定义所在模块(文件)的作用域  Global(module)  G
Python内建模块的作用域     Builtin(python)    B

变量名的查找规则
   L --->  E  ---> G  ---->  B
   注:
     在默认的情况下,变量名赋值会创建或改变当前作用域
     内变量的绑定关系


# 此示例示意作用域
v = 100
def f1():
    # v = 200
    print("f1.v=", v)
    def f2():
        v = 300
        print("f2.v=", v)
    f2()
f1()
print("v=", v)




