# file_write_binary.py


# 此示例示意二进制文件的写操作
try:
    # 二进制写操作
    f = open("zhang.txt", 'wb')

    # f.write(b"hello")  # 出错
    b = bytes("张奔",'utf-8')
    print(b)
    f.write(b)

    f.close()
except OSError:
    print("打开文件失败!")

