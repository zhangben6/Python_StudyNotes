# return_function.py

def get_function():
    s = input("请输入您要做的操作: ")
    if s == "求最大":
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2, 4, 6, 8, 10]
fx = get_function()
v = fx(L)
print(v)
