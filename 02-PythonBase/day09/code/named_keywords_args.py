# named_keywords_args.py


# 此示例示意命名关键字形参
def func(a, b, *, c, d):
    print(a, b, c, d)

# func(1, 2, 3, 4)  # 传参失败
# func(1, 2, c=30, d=40)
func(a=10, b=20, c=30, d=40)
# func(1, 2, **{'d':400, 'c':300})

