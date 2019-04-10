# 练习:
#   任意输入一段字符串
#     1) 计算出字符串中空格的个数
#     2) 计算出字符串中中文字符的个数
#        (注: 中文 字符的编码值一定大于128,可用ord判断)

x = input('请输入一段文字: ')
# 1.计算空格的个数
# print("空格的个数是:", x.count(' '))
blank_count = 0
for c in x:
    if c == ' ':
        blank_count += 1
print("空格的个数是:", blank_count)

# 2. 计算中文字符的个数
chinse_count = 0
for c in x:
    if ord(c) > 128:
        chinse_count += 1
print("中文字符的个数是:", chinse_count)