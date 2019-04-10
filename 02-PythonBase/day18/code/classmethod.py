# classmethod.py

# class A:
#     v = 100 # 类变量

#     @classmethod
#     def get_v(cls):
#         '''这是一个类方法,用来获取类变量v的值'''
#         return cls.v

#     @classmethod
#     def set_v(cls, value):
#         cls.v = value

# print(A.get_v())  # 100 获取类变量v的值
# # A.v = 200
# A.set_v(200)
# print(A.get_v())  # 200

class A:
    v = 100
    @classmethod
    def getscore(cls):
        return cls.v
    
    @classmethod
    def setscore(cls,value):
        cls.v = value
print(A.getscore())
A.setscore(300)
print(A.getscore())