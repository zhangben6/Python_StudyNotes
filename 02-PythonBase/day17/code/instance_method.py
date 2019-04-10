# instance_method.py

# 此示例示意在类内定义实例方法的语法和调用方法
class Dog:
    def eat(self, food):
        print("id为", id(self),
              "的小狗正在吃", food)

    def sleep(self, hour):
        print('id为', id(self),
              '的小狗睡了', hour, '小时')

    def play(self, obj):
        print("id为", id(self),
              '的小狗正在玩', obj)

dog1 = Dog()  # 创建一个Dog类型的实例
dog1.eat("骨头")
dog1.sleep(1)  # 睡一个小时
dog1.play("球")

dog2 = Dog()
dog2.eat("狗粮")
dog2.sleep(3)
dog2.play('飞盘')

# 以下示意用类名来调用实例方法
Dog.eat(dog1, "包子")  # 等同于 dog1.eat("包子")
Dog.eat(dog2, "猫粮")  # 等同于 dog2.eat("猫粮")


# lst1 = list()
# lst1.append(10)  # 调用方法