
#  2. 写一个程序,任意输入一个整数,判断这个整数是否是素数(prime)
#    素数(也叫质数), 只能被1和自身整除的正整数
#      如:   2 3 5 7 11 13 17 19
#     提示:
#       用排除法,当判断x是否为素数时,只要让x分别除以
#       2, 3, 4, ... x-1 ,只要有一个能整除,则x不是
#       素数,否则x是素数

x = int(input("请输入一个整数: "))
if x < 2:
    print(x, '不是素数')
else:
    prime_flag = True  # 先假设x是素数
    for i in range(2, x):
        if x % i == 0:  # 说明整数
            prime_flag = False
            break
    # 当循环结束后,prime_flag 为真则为素数
    if prime_flag:
        print(x, "是素数")
    else:
        print(x, "不是素数")