
# 练习:
#   写程序输入一个字符串,打印字符串中的如下内容
#     1. 打印这个字符串的第一个字符
#     2. 打印这个字符串的最后一个字符
#     3. 如果这个字符串的长度是奇数，打印中间这个字符
#   注:
#     求字符串长度的函数是 len(s)

# s = input("请输入一个字符串: ")
# if s:
#     print("第一个字符是:", s[0])
#     print("最后一个字符是:", s[-1])
#     if len(s) % 2 == 1:
#         center = len(s) // 2
#         print("中间这个字符是:", s[center])
# else:
#     print("您输入的字符串为空，不能计算")
n = 'hello'
if len(n) % 2 == 1:
    center = len(n) // 2
    print(n[center])