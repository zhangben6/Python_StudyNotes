#   1. 写一个程序，输入一个数，用if语句计算出这个数的
#     绝对值并打印出来

k = int(input("请输入一个整数: "))

# 方法1
# if n > 0:
#     r = n
# else:
#     r = -n

# 方法2
# r = n
# if r < 0:
#     r = -r

# print(n,'的绝对值是:', r)

money = 13
if k > 3:
    money = money + (k-3)*2.3
if k > 15:
    money = money + (k-15) * 3.45
print('费用为%.2f元' % money)

