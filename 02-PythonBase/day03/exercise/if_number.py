# 练习:
#   任意输入一个整数
#     1) 判断这个数是否大于100
#     2) 判断这个数是否小于0
#     3) 判断这个数是否在50~150之间
#     (建议每一步用一个if语句来实现)

s = input("请输入一个整数: ")
n = int(s)  # 转为整数
# 1) 判断这个数是否大于100
if n > 100:
    print(n, '是大于100的')
else:
    print(n, '不大于100')

# 2) 判断这个数是否小于0
if n < 0:
    print(n, '是小于0的')
else:
    print(n, '不小于0')

# 3) 判断这个数是否在50~150之间
if 50 < n < 150:
    print(n,'是50~150之间')
else:
    print(n,'不在50~150之间')

