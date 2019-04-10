# file_read_text1.py

# 此示例示意以每次读取一行的形式读取文本文件内容
try:
    # 1. 打开文件
    # myf = open('myfile.txt')  # 相对路径,相对code
    myf = open('/home/tarena/aid1809/pbase/day16/code/myfile.txt')  # 绝对路径

    # 2. 读/写文件
    line1 = myf.readline()  # line='ABCD\n'
    print("此行长度是:%d, 内容是:" % len(line1), line1)
    line2 = myf.readline()
    print("第二行是:", line2)
    line3 = myf.readline()
    print("第三行是:", line3)
    line4 = myf.readline()  # line4=''
    if line4 == '':
        print('已到文件末尾!')
    # 3. 关闭文件
    myf.close()
except OSError:
    print("文件打开失败")


