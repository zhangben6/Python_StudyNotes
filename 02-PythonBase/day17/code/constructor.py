# constructor.py

# 此示例示意最基础的类的定义
class Dog:  # 此语句的含义是创建一个Dog类用变量Dog绑定
    pass


# 调用构造函数来创建实例对象
dog1 = Dog()  # dog1绑定的是一个Dog类的对象
print("id(dog1)=", id(dog1))
dog2 = Dog()  # dog2绑定的是另一个Dogr类的对象
print("id(dog2)=", id(dog2))

lst1 = list()  # lst1 绑定一个列表
print('id(lst1)=', id(lst1))
lst2 = list()  # lst2 绑定另一个列表
print('id(lst2)=', id(lst2))

