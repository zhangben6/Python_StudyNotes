# file_read_binary.py

# 此示例示意用二进制文件操作来读取文本文
# 件里的内容

try:
    f = open('myfile.txt', 'rb')
    b = f.read(5)  # b绑定字节串
    print(b)
    print("字节串的长度是:", len(b))
    b2 = f.read()
    print(b2)
    print("字节串b2的长度是:", len(b2))

    b3 = f.read()  # b3 绑定空字节串
    print(b3 == b'')  # True
    f.close()
    # 将b2的内容转为字符串打印:
    s = b2.decode('utf-8')
    print(s)
    print("字符串s的长度是:", len(s))

except OSError:
    print("打开读文件失败!")
