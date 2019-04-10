# with2.py

# 此示例示意将自定义的类变为环境管理器,
# 让自定义的类创建的对象能用在with语句中
# 环境管理器
#   类内有 __enter__ 和 __exit__实例方法的类被称为
#   环境管理器
#   __enter__将在进入with语句时被调用,并返回由as变量
#   管理的对象
#   __exit__将在离开with语句时被调用,且可以用参数来
#   判断在离开with语句时是否有异常发生,并做出相应的
#   处理
# 示例见:
#   with2.py

class A:
    def __enter__(self):
        '''此方法必须返回由 as 绑定的对象'''
        print("A类对象已进入with语句")
        return self

    def __exit__(self, e_type, e_value, e_tb):
        '''e_type绑定异常类型,没有异常时绑定None
        e_value 绑定错误对象,没有异常时绑定None
        e_tb 绑定追踪对象,没有异常时绑定None
        '''
        print("A类对象已离开with语句")
        if e_type is None:
            print("我是没有异常时退出的with语句")
        else:
            print("有离开with语句时有异常发生")
            print(e_type)
            print(e_value)
            print(e_tb)
try:
    with A() as a:
        print("这是with语句内部的一条语句")
        int(input("请输入整数: "))
        
except:
    print("出现错误")
print(a)
print("程序正常退出")






