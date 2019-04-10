# classmethod.py

class A:
    v = 100 # 类变量

    @classmethod
    def get_v(cls):
        '''这是一个类方法,用来获取类变量v的值'''
        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value

print(A.get_v())  # 100 获取类变量v的值

a1 = A()
# 类和该类的实例都可以调用类方法
print(a1.get_v())  # 该类的实例可以调用类方法
a1.set_v(300)
print(a1.get_v())  # 300
print(A.get_v())  # 300
