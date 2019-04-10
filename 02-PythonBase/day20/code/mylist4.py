
# 此示例示意 一元 运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return "MyList(%s)" % self.data
    
    def __neg__(self):
        a = [-x for x in self.data]
        return MyList(a)

    def __pos__(self):
        a = [abs(x) for x in self.data]
        return MyList(a)

L = MyList([1, -2, 3, -4, 5])
L2 = -L  # 
print(L2)  # MyList([-1, 2, -3, 4, -5])
L3 = +L
print(L3)   # MyList([1, 2, 3, 4, 5])

