

try:
    # myf = open('myfile.txt')  # 相对路径,相对code
    myf = open('/home/tarena/aid1809/pbase/day16/code/myfile.txt')  # 绝对路径

    # 2. 读/写文件
    s1 = myf.read(5)
    print(s1)  # s1='ABCD\n'
    s2 = myf.read(2)  # s2='12'
    print(s2)
    s3 = myf.read()  # s3='34\n这是中文\n'
    print(s3)
    s4 = myf.read()  # s4='' 空字符串
    print(s4 == '')  # True

    # 3. 关闭文件
    myf.close()
except OSError:
    print("文件打开失败")


