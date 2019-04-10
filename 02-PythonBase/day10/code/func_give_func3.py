def myinput(fn):
    L = [1, 3, 9, 5, 7]
    return fn(L)

print(myinput(max))  # 9
print(myinput(min))  # 1
print(myinput(sum))  # 25
