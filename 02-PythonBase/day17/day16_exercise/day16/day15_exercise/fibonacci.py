#   2. 写一个生成器函数fibonacci, 生成斐波那契数的前n
#      个数
#      1 1 2 3 5 8 ....
#      如:
#         def fibonacci(n):
#             ...
#             yield ...
#             ...
#       1) 打印前20个数:
#         for x in fibonacci(20):
#             print(x)
#       2) 打印前40个斐波那契数的和
#         print(sum(fibonacci(40))) 

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        # 此处的语句会执行 n次,每执行一次生成一个数
        yield b
        a, b = b, a + b

# 1) 打印前20个数:
for x in fibonacci(20):
    print(x)
# 2) 打印前40个斐波那契数的和
print(sum(fibonacci(40))) 
