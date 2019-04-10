# multi_inherit2.py

# 小张写了一个类A
class A:
    def m(self):
        print("A.m()被调用")

# 小李写了一个类B
class B:
    def m(self):
        print("B.m()被调用")

class AB(B, A):
    pass
    # def m(self):
    #     print("AB.m()")

ab = AB()
ab.m()  # 请问如何调用?
print(AB.__mro__)