# named_keywords_args.py


# 此示例示意命名关键字形参
def func(a, b, *args, c, d):
    print(a, b, args, c, d)

# func(1, 2, 3, 4)  # 传参失败
func(1, 2, c=30, d=40)
func(1, 2, 3, 4, 5, d=400, c=300)

