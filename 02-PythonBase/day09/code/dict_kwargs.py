# dict_kwargs.py


# 此示例示意双星号字典形参
def func(**kwargs):
    print("关键字传参的个数是:", len(kwargs))
    print('kwargs=', kwargs)

func(name="魏老师", age=35, address="朝阳区")

def func(*,a, b, **kwargs):
    print("关键字传参的个数是:", len(kwargs))
    print('kwargs=', kwargs)

func(a=1, b=2, c=3, d=4)
