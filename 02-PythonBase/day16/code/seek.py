# seek.py

# 此示例示意用随机定位的方式读取myfile2.txt文件中的内容

try:
    f = open('student_info.txt', 'rb')
    print("新打开的文件的读写位置是:", f.tell()) # 0

    b = f.read(2)  # 读取两个字节后
    print("读两个字节后的文件读写位置是:", f.tell())
    print("读取的内容是:", b)

    # 以下用seek方法让读写位置定位到5的位置
    # f.seek(5, 0)  # 从文件头向后5个字节
    # f.seek(3, 1)  # 从当前位置向后移动3个字节
    f.seek(-15, 2)  # 从文件尾前移动15个字节


    print("移动的后位置是:", f.tell())  # 5
    b2 = f.read(5)
    print("b2=", b2)  # b'abcde'
    f.close()
except OSError:
    print("打开文件失败")