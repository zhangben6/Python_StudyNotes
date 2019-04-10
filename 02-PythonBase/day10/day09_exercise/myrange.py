#  5. 写一个myrange函数,参数可以传1~3个,实际含义
#     与range函数规则相同,此函数返回符合range函数规则
#     的列表
#     如:
#       L = myrange(4)
#       print(L)  # [0, 1, 2, 3]
#       L = myrange(4, 6)
#       print(L)  # [4, 5]
#       L = myrange(1, 10, 3)
#       print(L)  # [1, 4, 7]

# def myrange(start,stop=None,step=1):
#     if step > 0:
#         if stop is None:
#             stop = start
#             start = 0
#         L = [x for x in range(start,stop,step)]
#     elif step < 0:
#         L = []
#         while start > stop:
#             L.append(start)
#             start += step
#     return L
# print(myrange(5))















# def myrange(start, stop=None, step=1):
#     # 先判断stop是否为None,如果为None说明start为结束值
#     if step > 0:
#         if stop is None:
#             stop = start
#             start = 0
#         L = [x for x in range(start, stop,step)]
#     elif step < 0:
#         L = []
#         while start > stop:
#             L.append(start)
#             start += step

#     return L


# L = myrange(4)
# print(L)  # [0, 1, 2, 3]
# L = myrange(4, 6)
# print(L)  # [4, 5]
# L = myrange(1, 10, 3)
# print(L)  # [1, 4, 7]
# L = myrange(10, 0, -3)
# print(L)  # [10, 7, 4, 1]