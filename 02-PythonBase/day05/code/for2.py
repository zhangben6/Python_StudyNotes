# for.py

# 此示例示意for语句的用法

s = "ABCDE"
for ch in s:
    print("ch---->", ch)
    if ch == 'C':
        break
    print("这是break之后的语句")
else:
    print("for语句的else子句被执行")

print("程序结束")


