# 1. 打印 1 ~ 20的整数，打印在一行(用for语句实现)
for x in range(1, 21):
    print(x, end=' ', flush=True)
print()  # 换行

# 2. 计算 1 + 2 + 3 + 4 + ..... + 99 + 100的和
#     (用for和range实现)
s = 0
for x in range(1, 101):
    s += x
print("1+2+3+4+....+100的和是:", s)

# 3. 计算 1 + 3 + 5 + 7 + .... + 97 + 99的和
# 　　(用for语句实现)
s = 0
for x in range(1, 101, 2):
    s += x
print("1+3+5+....+99的和是:", s)

