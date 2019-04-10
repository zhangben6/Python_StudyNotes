
from student import Student

def input_student():
    # 此函数用于返回所有用户输入的学生信息的列表
    infos = []  # 创建一个列表容器准备存放每个学生信息的字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果姓名为空,则结束输入
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
        except:
            print("输入有错,请重新输入!")
            continue
        d = Student(n, a, s)  # 学生对象
        infos.append(d)
    return infos

def output_student(L):
    # 此函数以表格形式打印学生信息
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for d in L:  # d绑定字典
        n, a, s = d.get_infos()
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
        if L[i].get_name() == n:
            del L[i]  # 删除索引
            print("删除成功!")
            return # 删除完毕
        i += 1
    print("删除失败")

def modify_student_score(L):
    n = input("请输入要修改成绩的人的姓名: ")
    s = int(input("请输入新成绩: "))
    print(".....")

def output_student_by_score_desc(L):
    # 生成一个排序后的新列表
    def k(d):  # 传入的是字典,返回的是成绩
        return d.get_score()
    lst = sorted(L, key=k, reverse=True)
    output_student(lst)

def output_student_by_score_asc(L):
    lst = sorted(L, key=lambda d: d.get_score())
    output_student(lst)

def output_student_by_age_desc(L):
    lst = sorted(L,
                 key=lambda d: d.get_age(),
                 reverse=True)
    output_student(lst)

def output_student_by_age_asc(L):
    lst = sorted(L, key=lambda d: d.get_age())
    output_student(lst)

def read_from_file(filename='si.txt'):
    '''此函数返回
    [{'name':"小张", 'age':20, 'score':100},
    ...]'''
    L = []  # 此列表用于存储字典
    try:
        file = open(filename)  # 打开文件
        # 读取内容,把数据加入到列表中
        while True:
            s = file.readline()
            if not s:
                break
            # 用字符串s得到,姓名,年龄,成绩信息
            s = s.strip()  # 去掉末尾的换行符
            lst = s.split(',')  # lst=['小张', '20', '100']
            name, age, score = lst  # 序列赋值
            age = int(age)  # 转为整数
            score = int(score)
            L.append(Student(name,age,score))
        file.close()  # 关闭文件
    except OSError:
        print("打开文件失败")
    return L
print(read_from_file())

def save_to_file(L, filename='si.txt'):
    '''此函数用于把L中的信息存到filename文件中,
    格式为:
        张三,20,100
        李四,18,98
        小王,22,95
    '''
    try:
        f = open(filename, 'w')
        try:
            # 循环写入数据
            for d in L:
                d.write_to_file(f)
        finally:
            f.close()
    except OSError:
        print("保存失败!")





