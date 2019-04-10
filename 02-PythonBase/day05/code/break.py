# break.py

# 此示例示意用break语句来终止循环
i = 1
while i < 6:
    print("循环开始时的i=", i)
    if i == 3:
        break  # 用break来终止当前循环
    print("循环结束时的i=", i)
    i += 1
else:
    print("while里的else子句被执行")

print("程序结束")

