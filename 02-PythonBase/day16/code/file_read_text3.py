# file_read_text1.py

# 此示例示意以每次读取一行的形式读取文本文件内容
try:
    # 1. 打开文件
    myf = open('student_info.txt')  # 相对路径,相对code
    # myf = open('/home/tarena/aid1809/pbase/day16/code/myfile.txt')  # 绝对路径

    # 2. 读/写文件
    s1 = myf.read()
    print(s1)
    print("读到的字符个数是: ",len(s1))

    print("s1的字符串的python表达式是:", repr(s1))

    # 3. 关闭文件
    myf.close()
except OSError:
    print("文件打开失败")


