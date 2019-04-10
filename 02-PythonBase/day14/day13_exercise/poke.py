# 1. 模拟斗地主发牌,牌共54张
#    黑桃('\u2660'), 梅花('\u2663'), 红桃('\u2666')
#    方块('\u2665')
#    A2-10JQK
#    大王,小王
#    三个个,每人发17张牌,底牌留三张
#      输入回车,打印第1个人的17张牌
#      输入回车,打印第2个人的17张牌
#      输入回车,打印第3个人的17张牌
#      输入回车,显示三张底牌


kinds = ['\u2660', '\u2663', '\u2666', '\u2665']
numbers = ['A']
numbers += [str(x) for x in range(2, 11)]
numbers += list("JQK")
# print(numbers)
poke = ['大王', '小王']
for x in kinds:
    for y in numbers:
        poke.append(x + y)

# print(poke)
assert len(poke) == 54, '牌数不够'

import random
poke2 = poke.copy() # 复制另一幅牌
random.shuffle(poke2)
# print(poke2)

player1 = poke2[:17]
player2 = poke2[17:34]
player3 = poke2[34:51]
base = poke2[51:]

input()
print("第1个人的牌是:", player1)
input()
print("第2个人的牌是:", player2)
input()
print("第3个人的牌是:", player3)
input()
print("底牌是:", base)

