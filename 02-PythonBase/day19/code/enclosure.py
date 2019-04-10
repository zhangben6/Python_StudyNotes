# enclosure.py

# 此示例示意用私有实例变量和私有属性来演示封装

class A:
    def __init__(self):
        self.__ppp = 100  # 创建私有属性
        self.ppp = 200  # 非私有属性
    
    def __m(self):  # 私有方法
        print("私有方法__m() 被调用!")

    def test(self):
        print("__ppp属性的值为:", self.__ppp)
        self.__m()

a = A()
# print(a.__ppp)  # 出错,不允许访问私有属性
print(a.ppp)  # 200
a.test()  #
# a.__m()  # 出错.不允许调用私有方法


    

