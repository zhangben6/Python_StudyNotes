#   输入一段字符串，打印出这个字符串中出现过的字符及出现过
#   的次数
#     如:
#       输入: abcdabcaba
#     打印如下:
#       a: 4次
#       b: 3次
#       d: 1次
#       c: 2次
#     注: 不要求打印顺序

s = input("请输入文字: ")
d = {}  # 空字典用来记录字符及对应的个数
        # 键为字符，值为个数(最小值为1)

for ch in s:
    # print(ch)  # 遍历所有字符
    if ch not in d:  # ch不在字典中,第一次出现
        d[ch] = 1
    else:  # 已经存在
        d[ch] += 1

for k, v in d.items():
    print(k, ":", v, "次")

print("-------------------")
for t in d.items():
    print('t =', t)
    print("%s:%d次" % t)


