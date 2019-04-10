
# 此示例示意 复合赋值算术运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    
L1 = MyList(range(1, 4))

L5 = L1 * 2
print(L5)  # MyList([1, 2, 3, 1, 2, 3])

L6 = 2 * L1   # L1.__rmul__(2)
print(L6)