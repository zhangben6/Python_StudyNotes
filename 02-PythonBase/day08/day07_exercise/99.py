#   3. 打印九九乘法表:
#      1x1=1
#      1x2=2 2x2=4
#      1x3=3 2x3=6 3x3=9
#      ....
#      ......................9x9=81

for line in range(1, 10):  # line代表当前行
    # 打印第line行
    for x in range(1, line + 1):  # x 代表被乘
        print("%dx%d=%d" % (x, line, x*line),
              end=' ')
    print()  # 一行完成,再换行