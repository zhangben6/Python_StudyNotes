# variable_args2.py


# L = [1, 2, 3]
# def f1(L):
#     # L = [4, 5, 6]  # 赋值语句的作用是创建和或改变变量的绑定关系
#     L.append("ABC")
#     print(L)  # [1, 2, 3, "ABC"]

# f1(L)
# print(L)  # [1, 2, 3, "ABC"]

L = [1,2,3]
def f1(L):
    L =  [1,2,3] #又重新定义了一个局部变量
    L.append('ab')
    print(L)
f1(L)
print(L)