# file_open.py
# with语句
#   语法:
#     with 表达式1 [as 变量1],
#                表达式2[as 变量2], ...:
#         语句块
#   作用:
#     使用于对资源进行访问的场合,确保使用过程中不管
#     是否发生异常,都会执行必须的'清理'操作,并释放资
#     源（关闭操作)
#       如:文件使用后自动关闭,线程中锁的自动获取和
#            释放等
#   说明:
#     执行表达式, 用as 子句中的变量绑定生成的对象
#     with语句并不改变异常的状态
#   示例见:
#     with.py


# 此示例示意在文件操作过程中,用with来代替
# try-finally 句来关闭文件
try:
    # fr = open('myfile.txt', 'rt')
    with open('myfile.txt', 'rt') as fr:
        s = fr.readline()
        print("第一行的长度是:", len(s))
        int(input("请输入整数: "))  # 可能发生异常
except OSError:
    print("文件打开失败")

