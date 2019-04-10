# student.py

# 此文件定义一个类．此类记录学生对象的行为及属性
class Student:
    def __init__(self, n, a, s):
        self.__name = n
        self.__age = a
        self.__score = s

    def get_infos(self):
        '''此方法返回当前对象自己的信息的元组'''
        return (self.__name,
                self.__age,
                self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def set_score(self, s):
        assert 0 <= s <= 100, '成绩失败!'
        self.__score = s
    
    def get_age(self):
        return self.__age
    
    def write_to_file(self, file):
        file.write(self.__name)
        file.write(",")
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')
