
# in / not in 运算符重载
#        方法名             运算符和表达式
#  __contains__(self, e)    e in self    

# 此示例示意 in / not in  运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return "MyList(%s)" % self.data
    
    def __contains__(self, e):
        return e in self.data

L = MyList([1, -2, 3, -4, 5])
print(3 in L)  # True
print(3 not in L)  # False
print(100 in L)   # False
print(100 not in L)  # True

