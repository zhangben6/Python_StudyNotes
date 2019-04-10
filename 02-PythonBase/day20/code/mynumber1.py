# # mynumber1.py
# # 运算符重载
# #   什么是运算符重载
# #     让自定义的类生成的对象(实例)能够使用运算
# #     符进行操作
# #   作用:
# #     让自定义的类的实例像内建对象一样使用运算符
# #     让程序简洁易读
# #     对自定义的对象将运算符赋予新的运算规则
# # 算术运算符重载
# #   方法名                运算符和表达式   说明
# #  __add__(self, rhs)      self +  rhs  加法
# #  __sub__(self, rhs)      self -  rhs  减法
# #  __mul__(self, rhs)      self *  rhs  乘法
# #  __truediv__(self, rhs)  self /  rhs  除法
# #  __floordiv__(self, rhs) self // rhs  地板除
# #  __mod__(self, rhs)      self %  rhs  求余
# #  __pow__(self, rhs)      self ** rhs  幂运算

# #     rhs (right hands side)  右手边
# # 示例见:

# 此示例示意让自定义的类使用运算符进行操作
class MyNumber:
    def __init__(self, v):
        self.data = v

    def __str__(self):
        return "MyNumber(%d)" % self.data
    
    def __add__(self, other):
        print('__add__方法被调用')
        v = self.data + other.data
        return MyNumber(v)  # 创建一个新对象并返回

    def __sub__(self, rhs):
        return MyNumber(self.data - rhs.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1 + n2  # 等同于 n3 = n1.__add__(n2)
print(n1, '+', n2, '=', n3)
print(n1, '-', n2, '=', n1 - n2)

# class MyNumber():
#     def __init__(self,num):
#         self.data = num
#     def __add__(self,other):
#         v = self.data + other.data
#         return MyNumber(v)
#     def __repr__(self):
#         return "MyNumber(%d)" % (self.data)
#     def __sub__(self,other):
#         v = self.data - other.data
#         return MyNumber(v)
#     def __mod__(self,other):
#         v = self.data % other.data
#         return MyNumber(v)

# n1 = MyNumber(100)
# n2 = MyNumber(200)
# k1 = MyNumber(10)
# K2 = MyNumber(3)
# n3 = n1 + n2 # 相当于n1.__add__(n2)
# print(n3)
# n4 = n1-n2
# print(n4)
# K3 = k1 % K2
# print(K3)






# # 复合赋值算术运算符重载
# #   以复合赋值算术运算符 x += y 为例,此运算符会优先
# #   调用 x.__iadd__(y) 方法.如果没有__iadd__方法
# #   时会将赋合赋值运算符拆解为 x = x + y 然后再调用
# #   x = x.__add__(y)  方法,如果再不存在__add__方法
# #   则会触发TypeError异常
# #   其它复合赋值算术运算符也具有相同的规则

# #   方法名                运算符和表达式   说明
# #  __iadd__(self, rhs)      self +=  rhs  加法
# #  __isub__(self, rhs)      self -=  rhs  减法
# #  __imul__(self, rhs)      self *=  rhs  乘法
# #  __itruediv__(self, rhs)  self /=  rhs  除法
# #  __ifloordiv__(self, rhs) self //= rhs  地板除
# #  __imod__(self, rhs)      self %=  rhs  求余
# #  __ipow__(self, rhs)      self **= rhs  幂运算



# # 此示例示意 复合赋值算术运算符的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return "MyList(%s)" % self.data

#     def __add__(self, rhs):
#         print("__add__:", self, rhs)
#         return MyList(self.data + rhs.data)

#     def __iadd__(self, rhs):
#         print("__iadd__被调用")
#         self.data.extend(rhs.data)
#         return self  # 返回自身


# L1 = MyList([1, 2, 3])
# L2 = MyList([4, 5, 6])
# print("id(L1)=", id(L1))
# L1 += L2  # 优先 L1.__iadd__(L2) 第二步才 L1 = L1.__add__(L2)
# print("id(L1)=", id(L1))
# print(L1)   


# # 一元运算符的重载
# #   方法名          运算符和表达式  说明
# #  __neg__(self)     - self      负号
# #  __pos__(self)     + self      正号
# #  __insert__(self)  ~ self      取反


# # 此示例示意 一元 运算符的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return "MyList(%s)" % self.data
    
#     def __neg__(self):
#         a = [-x for x in self.data]
#         return MyList(a)

#     def __pos__(self):
#         a = [abs(x) for x in self.data]
#         return MyList(a)

# L = MyList([1, -2, 3, -4, 5])
# L2 = -L  # 
# print(L2)  # MyList([-1, 2, -3, 4, -5])
# L3 = +L
# print(L3)   # MyList([1, 2, 3, 4, 5])




# # in / not in 运算符重载
# #        方法名             运算符和表达式
# #  __contains__(self, e)    e in self    

# # 此示例示意 in / not in  运算符的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return "MyList(%s)" % self.data
    
#     def __contains__(self, e):
#         return e in self.data

# L = MyList([1, -2, 3, -4, 5])
# print(3 in L)  # True
# print(3 not in L)  # False
# print(100 in L)   # False
# print(100 not in L)  # True



# 索引和切片运算符的重载
#   L[0]
#   L[::2]
#  方法名                  运算符和表达式  说明
#  __getitem__(self, i)    x = self[i]  取值
#  __setitem__(self, i, v) self[i] = v  赋值
#  __delitem__(self, i)    del self[i]  删除索引

# # 此示例示意 索引和切片  运算符的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return "MyList(%s)" % self.data
    
#     def __getitem__(self, i):
#         print("__getitem__被调用, i=", i)
#         return self.data[i]

#     def __setitem__(self, i, v):
#         print("__setitem__被调用, i=", i, 'v=', v)
#         self.data[i] = v

#     def __delitem__(self, i):
#         del self.data[i]
# L = MyList([1, -2, 3, -4, 5])
# v = L[2]  # L.__getitem__(2)
# print('v=', v)
# L[1] = 2.222  # L.__setitem__(1, 2.2222)
# print(L)  # MyList([1, 2.222, 3, -4, 5])

# del L[3]  # 调用L.__delitem__(3)
# print(L)  # MyList([1, 2.222, 3, 5])



# # slice 构造函数
# #   作用:
# #     用于创建一个slice切片对象,此对象存储一个切片
# #     的起始值,终止值和步长信息,默认都为None
# #   格式:
# #     slice(start=None, stop=None, step=None)
# #   slice对象的属性
# #     s.start 切片的起始值 默认为None
# #     s.stop  切片的终止值,默认为None
# #     s.step  切片的步长,默认为None


# # 此示例示意 索引和切片  运算符的重载
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return "MyList(%s)" % self.data
    
#     def __getitem__(self, i):
#         print("__getitem__被调用, i=", i)
#         if type(i) is int:
#             print("您正在执行索引操作")
#         elif type(i) is slice:
#             print("您正在执行切片操作")
#             print(i.start, i.stop, i.step)
#         return self.data[i]

#     def __setitem__(self, i, v):
#         print("__setitem__被调用, i=", i, 'v=', v)
#         self.data[i] = v

#     def __delitem__(self, i):
#         del self.data[i]

# L = MyList([1, -2, 3, -4, 5])
# print(L[::2])

