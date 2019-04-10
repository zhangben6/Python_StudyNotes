# lambda.py

# 此示例示意lambda 表达式的语法和用法
# def myadd(x, y):
#     return x + y

# print("4 + 5 =", myadd(4, 5))  # 9


print("4 + 5 =", (lambda x, y: x + y)(4, 5))  # 9
