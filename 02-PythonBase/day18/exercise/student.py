# 练习:
#   1. 用类来描述一个学生的信息(也可以改写之前的
#      Student类)
#   2. 学生信息有:
#      姓名,年龄,成绩
#   3. 将这些学生对象存于列表中,可以任意添加,和
#      删除学生信息
#    1) 打印出学生的个数
#    2) 打印出所有学生的平均成绩
#    3) 打印出所有学生的平均年龄
#      (建议用类变量来记录学生的信息的列表)

class Student:
    def __init__(self, n, a, s):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.score = s  # 成绩

infos = []  # 用于保存学生信息的列表

def add_student(infos):
    n = input("请输入学生姓名: ")
    a = int(input("请输入学生年龄: "))
    s = int(input("请输入学生成绩: "))
    infos.append(Student(n, a, s))

def del_student(infos):
    n = input("请输入要删除学生的姓名: ")
    for i, s in enumerate(infos):
        # 如果当前学生对象的姓名，与要删除学生姓名相同
        if s.name == n:
            del infos[i] # 删除此学生
            print("删除成功")
            return
    print("删除失败")

def print_student_count(infos):
    print('学生的个数是:', len(infos))

def print_student_avg_score(infos):
    score = 0
    for s in infos:
        score += s.score
    print("平均成绩是:", score / len(infos))

add_student(infos)
add_student(infos)
# add_student(infos)

del_student(infos)

add_student(infos)

#    1) 打印出学生的个数
print_student_count(infos)
#    2) 打印出所有学生的平均成绩
print_student_avg_score(infos)
