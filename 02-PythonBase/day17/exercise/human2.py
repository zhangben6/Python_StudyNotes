# 练习:
#   有两个人:
#     第一个人:  姓名:张三, 年龄:35岁
#     第二个人:  姓名:李四, 年龄:15岁
#   行为:
#     1. 教别人学东西  teach
#     2. 工作赚钱  work
#     3. 借钱 borrow
#     4. 显示自己的信息 show_info
#   事情:
#     张三 教 李四 学 python
#     李四 教 张三 学 王者荣耀
#     张三 上班赚了 1000 元钱
#     李四 向 张三 借钱 200 元
#     35 岁的 张三 有钱 800 元,它学会的技能是: 王者荣耀
#     15 岁的 李四 有钱 200 元,它学会的技能是: python

class Human:
    def __init__(self, n, a):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.money = 0  # 钱数
        self.skill = []  # 所学技能列表

    def teach(self, other, subject):
        other.skill.append(subject)
        print(self.name, '教', other.name,
             '学', subject)

    def work(self, money):
        self.money += money
        print(self.name, '上班赚了', money, '元钱')

    def borrow(self, other, money):
        if other.money > money:
            other.money -= money
            self.money += money
            print(self.name, '向', other.name, 
                '借钱', money, '元')
        else:
            print(other.name, '没有借钱给',
                  self.name)

    def show_info(self):
        print(self.age, '岁的', self.name,
              '有钱', self.money,
              '它学会的技能是:', self.skill)

zhang3 = Human("张三", 35)
li4 = Human("李四", 15)
# 张三 教 李四 学 python
zhang3.teach(li4, "Python")
# 李四 教 张三 学 王者荣耀
li4.teach(zhang3, '王者荣耀')
# 张三 上班赚了 1000 元钱
zhang3.work(1000)
# 李四 向 张三 借钱 200 元
li4.borrow(zhang3, 200)
# 35 岁的 张三 有钱 800 元,它学会的技能是: 王者荣耀
zhang3.show_info()
# 15 岁的 李四 有钱 200 元,它学会的技能是: python
li4.show_info()