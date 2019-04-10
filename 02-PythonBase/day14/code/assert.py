# assert.py


def get_score():
    s = int(input("请输入学生成绩:"))
    assert 0 <= s <= 100, '成绩超出范围'
    # 上一句等同于如下if语句
    # if bool(0 <= s <= 100) == False:
    #     raise AssertionError('成绩超出范围')
    return s

try:
    score = get_score()
    print("学生的成绩是:", score)
except AssertionError as err:
    print("发生错误,错误数据是:", err)
