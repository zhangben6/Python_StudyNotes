# mro.py
# 多继承的MRO(Method Resolution Order) 问题
#   MRO --> 方法的解决(查找)顺序
#   类的 __mro__属性
#     用来记录类的方法的查找顺序


class A:
    def go(self):
        print('A')
        # super().go()  # 出错

class B(A):
    def go(self):
        print('B')
        super().go()  # ????

class C(A):
    def go(self):
        print('C')
        super().go()

class D(C,B):
    def go(self):
        print("D")
        super().go()

d = D()
d.go()
print(D.__mro__)