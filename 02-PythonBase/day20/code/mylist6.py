
# 此示例示意 索引和切片  运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return "MyList(%s)" % self.data
    
    def __getitem__(self, i):
        print("__getitem__被调用, i=", i)
        return self.data[i]

    def __setitem__(self, i, v):
        print("__setitem__被调用, i=", i, 'v=', v)
        self.data[i] = v

    def __delitem__(self, i):
        del self.data[i]
L = MyList([1, -2, 3, -4, 5])
v = L[2]  # L.__getitem__(2)
print('v=', v)
L[1] = 2.222  # L.__setitem__(1, 2.2222)
print(L)  # MyList([1, 2.222, 3, -4, 5])

del L[3]  # 调用L.__delitem__(3)
print(L)  # MyList([1, 2.222, 3, 5])