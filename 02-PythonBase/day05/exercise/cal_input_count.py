# 让用户任意输入一些整数,当输入负数时结束输入
#   当输入完成后,打印您输入的这些数的和
#   如:
#     请输入: 1
#     请输入: 2
#     请输入: 3
#     请输入: 4
#     请输入: -1
#   打印: 10

s = 0
while True:
    n = int(input("请输入: "))
    if n < 0:
        break
    s += n
else:
    print("这行语句永远不会执行!!!")

print("和是:", s)
