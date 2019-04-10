#   输入一个字符串：
#     1. 判断您输入的字符有几个空格
#     2. 将原字符串的左右空白字符去掉，打印出有效的字符
#        个数
#     3. 判断您输入的是否是数字,
#         如果是数字，判断用户输入的数字是否大于100


s = input("请输入任意一个字符串: ")
k = s.count(' ')
print(k)
s2 = s.strip()

print(s2)
print(len(s2))


















# s = input("请输入任意一个字符串: ")
# blank_count = s.count(' ')
# print("空格的个数是:", blank_count)

# s2 = s.strip()  # 去掉左右空白字符
# print("去掉空白字符后", s2)
# print("有效字符的个数是:", len(s2))

# if s2.isdigit(): 
#     print("您刚才输入的是数字")
#     n = int(s2)  # 转为整数
#     if n > 100:
#         print("您刚才输入的数字大于100")
# else:
#     print("您输入的不是数字")

