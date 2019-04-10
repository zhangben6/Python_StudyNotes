# main.py

from menu import show_menu
from student_info import *

def main():
    '''主函数,此函数最先运行'''
    infos = []  # 此列表用来保存所有学生的信息的字典
    # 进入主事件循环
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            return  # 退出main函数
        elif s == '1':
            # infos += input_student()
            # infos.extend(input_student())
            input_student(infos)
        elif s == '2':
            output_student(infos)
        elif s == '3':
            remove_student(infos)
        elif s == '4':
            modify_student_score(infos)
        elif s == '5':
            output_student_by_score_desc(infos)
        elif s == '6':
            output_student_by_score_asc(infos)
        elif s == '7':
            output_student_by_age_desc(infos)
        elif s == '8':
            output_student_by_age_asc(infos)

main()  # 程序从此开始
