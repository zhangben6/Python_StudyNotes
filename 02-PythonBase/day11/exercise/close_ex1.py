# L = [lambda x: x*i,
#      lambda x: x*i,
#      lambda x: x*i,
#      lambda x: x*i,
#      ]

def get_funs(n):
    L = []
    for i in range(n):
        L.append(lambda x: x * i)
    return L

funs = get_funs(4)
print(funs[0](10))  # 30
print(funs[1](10))  # 30
print(funs[2](10))  # 30
print(funs[3](10))  # 30
