# file_read_text1.py

# 此示例示意以每次读取一行的形式读取文本文件内容
try:
    # 1. 打开文件
    # myf = open('myfile.txt')  # 相对路径,相对code
    myf = open('student_info.txt')  # 绝对路径

    # 2. 读/写文件
    L = myf.readlines()  # 把文件内容形成字符串列表返回回来
    print(L)
    # 3. 关闭文件
    myf.close()
except OSError:
    print("文件打开失败")


