# instance_attribute.py

# 此示例示意实例属性的创建及使用
class Dog:
    def eat(self, food):
        print(self.color, '的', self.kinds,
             '正在吃', food)
        # 在吃的过程中添加一个last_food属性用来记录
        # 此次吃的是什么
        self.last_food = food

    def show_info(self):
        print(self.color, '的', self.kinds,
              '上次吃的是', self.last_food)


dog1 = Dog()
dog1.color = "白色"  # 颜色
dog1.kinds = '京巴'  # 种类
dog1.eat('骨头')
# print(dir(dog1))
# print(dog1.color)

dog2 = Dog()
dog2.color = '灰色'
dog2.kinds = '哈士奇'
dog2.eat('狗粮')
# print(dir(dog2))

# 打印每个小狗现在的信息
dog1.show_info()  # 白色 的 京巴 上次吃的是 骨头
dog2.show_info()
