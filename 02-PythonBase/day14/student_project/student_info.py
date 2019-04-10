
# 2. 修改原学生信息管理程序,将程序拆分为模块:
#    要求:
#      1. 主事件循环while语句放在main.py中
#      2. show_menu函数放在menu.py中
#      3. 与学生操作相关的函数放在student_info.py中


def input_student(infos):
    # 此函数用于返回所有用户输入的学生信息的列表
    # infos = []  # 创建一个列表容器准备存放每个学生信息的字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果姓名为空,则结束输入
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        # 新创建一个字典 {}  dict()
        d = {'name':n, 'age':a, 'score':s}  # d = dict(name=n, age=a, score=s)
        infos.append(d)
    return infos

def output_student(L):
    # 此函数以表格形式打印学生信息
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for d in L:  # d绑定字典
        n = d['name']
        a = d['age']
        s = d['score']
        a = str(a)  # 将整数转为字符串
        s = str(s)
        print("|" + n.center(15) + '|'
                + a.center(11) + '|'
                + s.center(10) + '|')
    print("+---------------+-----------+----------+")

def remove_student(L):
    # 获取要删除人的姓名
    n = input("请输入要删除人的姓名: ")
    i = 0  # 开始索引
    while i < len(L):
        if L[i]['name'] == n:
            del L[i]  # 删除索引
            print("删除成功!")
            return # 删除完毕
        i += i

def modify_student_score(L):
    n = input("请输入要修改成绩的人的姓名: ")
    s = int(input("请输入新成绩: "))
    print(".....")

def output_student_by_score_desc(L):
    # 生成一个排序后的新列表
    def k(d):  # 传入的是字典,返回的是成绩
        return d['score']
    lst = sorted(L, key=k, reverse=True)
    output_student(lst)

def output_student_by_score_asc(L):
    lst = sorted(L, key=lambda d: d['score'])
    output_student(lst)

def output_student_by_age_desc(L):
    lst = sorted(L,
                 key=lambda d: d['age'],
                 reverse=True)
    output_student(lst)

def output_student_by_age_asc(L):
    lst = sorted(L, key=lambda d: d['age'])
    output_student(lst)





