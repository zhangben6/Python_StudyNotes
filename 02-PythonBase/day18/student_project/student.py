# student.py

# 此文件定义一个类．此类记录学生对象的行为及属性
class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def get_infos(self):
        '''此方法返回当前对象自己的信息的元组'''
        return (self.name,
                self.age,
                self.score)

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score
    
    def set_score(self, s):
        assert 0 <= s <= 100, '成绩失败!'
        self.score = s
    
    def get_age(self):
        return self.age
    
    def write_to_file(self, file):
        file.write(self.name)
        file.write(",")
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')
