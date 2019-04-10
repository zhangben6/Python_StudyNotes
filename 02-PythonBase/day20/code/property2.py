# property2.py


# 不加@property
class Student:
    def __init__(self, score=0):
        self.__score = score

    def set_score(self, v):
        '''setter'''
        assert 0 <= v <= 100, "成绩超出范围"
        self.__score = v

    def get_score(self):
        '''getter'''
        return self.__score

s = Student()
print(s.get_score())
s.set_score(99)
# s.set_score(1000)  # 报错
print(s.get_score())

# 特性属性 @property
#   实现其它语言所拥有的 getter 和 setter 功能

#   作用:
#     用来模拟一个属性
#     通过@property装饰器可以对模拟的属性赋值和取值
#       加以控制
#   示例见:
#     property.py


# 此示例示意用特性属性虚拟一个score属性.
# 来对设置分数加以限制
class Student:
    def __init__(self, score=0):
        self.__score = score

    @property
    def score(self):
        print('''getter''')
        return self.__score

    @score.setter
    def score(self, v):
        print('''setter''')
        assert 0 <= v <= 100, "成绩超出范围"
        self.__score = v


s = Student()
print(s.score)  # 取值
s.score = 99    # 正确赋值
# s.score = 10000  # 赋值报错
print(s.score)
