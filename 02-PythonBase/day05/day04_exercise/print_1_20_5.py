#   4. 用while循环打印 1 ~ 20的整数，每行打印5个，
#      打印4行,如:
#      1 2 3 4 5
#      6 7 8 9 10
#      ...

i = 1
while i <= 20:
    print(i, end=' ')
    if i % 5 == 0:
        print()
    # if i == 5 or i == 10 or i == 15 or i == 20:
    #     print()

    # if i == 5:
    #     print()  # 换行
    # elif i == 10:
    #     print()
    # elif i == 15:
    #     print()
    # elif i == 20:
    #     print()
    i = i + 1

print()  # 换行print(end='\n')