# flush.py


f = open("myflush.txt", 'w')
f.write("你好!")
f.flush()  # 强制清空缓冲区
input("请按回车键继续: ")

