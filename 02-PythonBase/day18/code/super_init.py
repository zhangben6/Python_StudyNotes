# super的应用'super().__init__()'
#   显式调用基类的初始化方法
#     当子类中实现了__init__方法，基类的__init__方法
#     将不会被自动调用.如果需要调用，则需要用super显式
#     调用.

class Human:
    def __init__(self, n, a):
        print("Human类的__init__被调用", n, a)
        self.name = n
        self.age = a
        # 显式调用object类的__init__方法
        super().__init__()
    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)

class Student(Human):
    def __init__(self, n, a, s=0):
        super().__init__(n, a)
        # self.name = n
        # self.age = a
        self.score = s
    def infos(self):
        super().infos()
        print("成绩: ", self.score)

s1 = Student('小李', 18, 98)
s1.infos()

