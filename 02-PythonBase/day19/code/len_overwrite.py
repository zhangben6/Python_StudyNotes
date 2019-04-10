# len_overwrite.py

class MyList:
    '''自定义一个容器类MyList,内部采用列表来
    存储内部的数据'''
    def __init__(self, iterable=()):
        # 相当于列表的复制
        self.data = [x for x in iterable]

    def __len__(self):
        '''此方法必须返回整数'''
        return len(self.data)

    def __abs__(self):
        L = [abs(x) for x in self.data]
        new = MyList(L)  # 创建一个新的MyList对象
        return new
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __reversed__(self):
        self.data.reverse()
        return MyList(self.data)
    
    def 
myl = MyList([1, -2, 3, -4])
print(myl)  # MyList([1, -2, 3, -4])
print(len(myl))  # myl.__len__()
print(abs(myl))  # MyList([1, 2, 3, 4])
print(reversed(myl))

# myl2 = MyList()  # 创建空的容器
# print(myl2)