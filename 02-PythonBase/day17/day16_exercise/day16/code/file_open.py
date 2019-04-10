# file_open.py


# 文件的基本操作分为三步:
try:
    # 1. 打开文件
    # myf = open('myfile.txt')  # 相对路径
    # myf = open("我是不存在的文件.txt")  # 出错
    filename = '/home/tarena/aid1809/pbase/day16/code/myfile.txt'
    myf = open(filename)  # 绝对路径
    print("文件打开成功")


    # 2. 读/写文件

    # 3. 关闭文件
    myf.close()
    print("文件已经关闭")
except OSError:
    print("文件打开失败")


