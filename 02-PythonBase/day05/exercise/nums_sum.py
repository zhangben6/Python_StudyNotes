# 练习:
#   求:1 ~ 100之间所有不能被 2, 3, 5, 7整除的数的和

s = 0

for x in range(1, 100):
    # 跳过能被2, 3, 5, 7 整除的数
    if x % 2 == 0:
        continue
    if x % 3 == 0:
        continue
    if x % 5 == 0:
        continue
    if x % 7 == 0:
        continue
    print(x)
    s += x

print("和是:", s)

