# 练习:
#   实现两个自定义的列表相加
#     class MyList:
#         def __init__(self, iterable=()):
#              ...
#         .....
#     L1 = MyList(range(1, 4))
#     L2 = MyList([4, 5, 6])
#     L3 = L1 + L2
#     print(L3)  # MyList([1, 2, 3, 4, 5, 6])
#     L4 = L2 + L1
#     print(L4)  # MyList([4, 5, 6, 1, 2, 3])
#     L5 = L1 * 2
#     print(L5)  # MyList([1, 2, 3, 1, 2, 3])
#     # 思考:
#     L6 = 2 * L2   # 可以吗?为什么?


class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)

L1 = MyList(range(1, 4))
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)  # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4)  # MyList([4, 5, 6, 1, 2, 3])
L5 = L1 * 2  # L1.__mul__(2)
print(L5)  # MyList([1, 2, 3, 1, 2, 3])
# 思考:
# L6 = 2 * L1   # 2.__mul__(L1)  出错





