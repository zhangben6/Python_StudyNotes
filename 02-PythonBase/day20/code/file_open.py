# file_open.py

try:
    fr = open('myfile.txt', 'rt')
    try:
        s = fr.readline()
        print("第一行的长度是:", len(s))
        int(input("请输入整数: "))  # 可能发生异常
    finally:
        fr.close()
except OSError:
    print("文件打开失败")

