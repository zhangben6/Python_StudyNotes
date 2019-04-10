
# 此示例示意 复合赋值算术运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        print("__add__:", self, rhs)
        return MyList(self.data + rhs.data)

    def __iadd__(self, rhs):
        print("__iadd__被调用")
        self.data.extend(rhs.data)
        return self  # 返回自身

L = MyList([1, 2, 3])
def f1(lst):
    lst += MyList([4, 5, 6])

f1(L)
print(L)  # MyList([1, 2, 3, 4, 5, 6])
