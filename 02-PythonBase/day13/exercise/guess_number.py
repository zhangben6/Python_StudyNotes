#   猜数字游戏:
#     让程序随机生成一个整数(0~100)之间,用变量x绑定
#     让用户循环输入整数用y绑定,打印猜数字结果
#        如果y > x 则提示用户"您猜大了"
#        如果y < x 则提示用户"您猜小了"
#        如果y 等于 x 则提求用户"恭喜您猜对了",然后退出
#        循环输入,并打印用户猜数字的次数
import random as r

def guess_number():
    x = r.randint(0, 100)
    times = 0  # 次数
    while True:
        y = int(input("请输入: "))
        times += 1  # 次数加1
        if y > x:
            print("您猜大了")
        elif y < x:
            print("您猜小了")
        else:  # 此处一定相等
            print("恭喜您猜对了!")
            print("您共猜了%d次" % times)
            break  # return

guess_number()
