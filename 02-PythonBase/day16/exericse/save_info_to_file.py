# 练习:
#    1. 写一个程序,输入很多人的姓名,年龄,成绩存于文件
#      'infos.txt'中
#      文件格式自己定义(建议用逗号(,)来分隔各信息)
#     完成输入后查看文件格式是不是您想要的格式
#     (用文本文件进行操作)

#     L = input_student()
#     def save_to_file(L, filename='infos.txt')
#         ..

#     save_to_file(L)

# from student_info import input_student

# L = input_student()
# print(L)

# def save_to_file(L, filename='info2.txt'):
#     '''此函数用于把L中的信息存到filename文件中,
#     格式为:
#         张三,20,100
#         李四,18,98
#         小王,22,95
#     '''
#     try:
#         f = open(filename, 'w')
#         try:
#             # 循环写入数据
#             for d in L:
#                 f.write(d['name'])
#                 f.write(",")
#                 f.write(str(d['age']))
#                 f.write(",")
#                 f.write(str(d['score']))
#                 f.write('\n')
#         finally:
#             f.close()
#     except OSError:
#         print("保存失败!")


# save_to_file(L)

