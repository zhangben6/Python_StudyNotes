

# 打印10以内的奇数(用for语句实现)
for n in range(0, 10):
    if n % 2 == 0:  # 如果是偶数则跳过
        continue
    print(n)

print('==========================')
# 用while语句实现
n = 0
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    print(n)
    n += 1

