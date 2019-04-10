# inherit.py

# 此示例示意单继承的用法
class Human:  # <<--等同于 class Human(object):
    def say(self, what):
        print("说:", what)
    def walk(self, distance):
        print("走了:", distance, "公里")

class Student(Human):
    def study(self, subject):
        print("学习:", subject)

class Teacher(Student):
    def teach(self, subject):
        print("教师对象正在教:", subject)


h1 = Human()
h1.say("天凉了！")
h1.walk(5)
print('-----------------------------------')
s1 = Student()
s1.walk(4)
s1.say("感觉有点累")
s1.study("面向对象")
print("===================================")

t1 = Teacher()
t1.teach("继承／派生")
t1.walk(6)
t1.say("终于到家了")
t1.study("转魔方")
print(Human.__base__)

print(Teacher.__base__)

