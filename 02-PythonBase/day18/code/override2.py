# override2.py

# 此示例示意显式调用父类的被覆盖方法
class A:
    def work(self):
        print("A.work被调用!")

class B(A):
    def work(self):
        '''此方法会覆盖父类中同名的方法'''
        print("B.work被调用")
        super().work()
    pass

b = B()
b.work()  # B.work
# A.work(b)  # A.work被调用, 借助于类来调用父类的方法


