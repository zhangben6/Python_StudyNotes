# slots.py

# 此示例示意__slots__ 列表的定义方法和用法
class Human:
    # 此__slots__列表让Human创建的对象只允许有
    # name 和 age 属性
    __slots__ = ['name', 'age']
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show_info(self):
        print(self.name, '今年',
              self.age, '岁')

h1 = Human("Tarena", 15)
h1.show_info()  # Tarena 今年 15 岁


# 此处会报错,因为此属性不在__slots__列表内
h1.Age = 16
h1.show_info()  # Tarena 今年 15 岁

# __slots__ 列表里的方法限定了类其他的方法不能使用
