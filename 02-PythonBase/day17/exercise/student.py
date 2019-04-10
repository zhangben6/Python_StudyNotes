# 练习:
#   写一个学生类Student类,此类用于描述学生信息,学生
#     信息有:  姓名,年龄,成绩(默认为0)
#   1) 为该类添加初始化方法,实现在创建对象时自动设置:
#      name, age, score 属性
#   2) 添加set_score方法,能为对象修改成绩信息
#   3) 添加show_info方法打印学生对象的信息
#   如:
#     class Student:
#         def __init__(....):
#             ....
#         def set_score(....):
#             ...
#         def show_info(...)
#             ...
#     L = []
#     L.append(Student('小张', 20, 100))
#     L.append(Student('小李', 18, 95))
#     L.append(Student('小钱', 19))
#     L[-1].set_score(70)
#     for s in L:
#         s.show_info()


class Student:
    def __init__(self, name, age, score=0):
        self.name = name
        self.age = age
        self.score = score

    def set_score(self, score):
        self.score = score

    def show_info(self):
        print("姓名:", self.name,
              '年龄:', self.age,
              '成绩:', self.score)

L = []
L.append(Student('小张', 20, 100))
L.append(Student('小李', 18, 95))
L.append(Student('小钱', 19))
# L[-1].set_score(70)
for s in L:
    s.show_info()
