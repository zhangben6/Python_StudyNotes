super函数
  super(cls, obj) 返回绑定超类的实例(要求obj必须是cls 类或cls子类的对象)
  super()   返回绑定超类的实例，等同于:
        super(__class__, 实例方法的第一个参数),
        必须用在方法内调用
　作用:
    借助super() 返回的实例间接调用父类的覆盖方法

# 此示例示意用super函数 调用父类的被覆盖方法
class A:
    def work(self):
        print("A.work被调用!")

class B(A):
    def work(self):
        '''此方法会覆盖父类中同名的方法'''
        print("B.work被调用")

    def mywork(self):
        ''''''
        # 1. 调用B 类的work
        # self.work()

        # 2. 调用父类的work
        super(B, self).work()

        super().work()  # 无参调用只能用在方法内
b = B()
b.work()
b.mywork()
super(B,b).work()




