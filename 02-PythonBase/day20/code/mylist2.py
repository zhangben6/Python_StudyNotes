
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


L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
print("id(L1)=", id(L1))
L1 += L2  # 优先 L1.__iadd__(L2) 第二步才 L1 = L1.__add__(L2)
print("id(L1)=", id(L1))
print(L1)   

