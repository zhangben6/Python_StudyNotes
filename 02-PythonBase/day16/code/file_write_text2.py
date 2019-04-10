# file_write_text.py


# 此示例示意用F.write 和 F.writelines方法进行文件
# 写操作
try:
    f = open("mynote.txt", 'x')  # 以写方式打开

    f.write("ABC中文")
    f.writelines(['123', 'abc', "结束"])
    f.write("!")

    f.close()
except OSError:
    print('打开写文件失败!')

