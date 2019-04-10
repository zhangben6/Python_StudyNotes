# 练习:
#   自己写一个文件"info.txt", 内部存储一些文字信息如下:
#     张三,20,100
#     李四,18,98
#     小王,22,95
#   写程序将这些数据读取出来,并以如下格式打印在屏幕终端上
#     张三 今年 20 岁,成绩是: 100
#     李四 今年 18 岁,成绩是: 98
#     小王 今年 22 岁,成绩是: 95

def read_info_from_file(filename='info.txt'):
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
            L.append(dict(name=name,
                          age=age,
                          score=score))


        file.close()  # 关闭文件
    except OSError:
        print("打开文件失败")
    return L

def print_info(L):
    for d in L:
        print(d['name'], '今年', d['age'],
              '岁,成绩是:',d['score'])

# L = read_info_from_file()
# L = read_info_from_file('/home/tarena/aid1809/pbase/day16/exericse/info.txt')
L = read_info_from_file('/home/tarena/aid1809/pbase/day16/exericse/info2.txt')
print_info(L)