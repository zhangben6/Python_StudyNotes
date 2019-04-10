# eval.py

s= "1 + 2 * 3 + 4"

v = eval(s)
print(v)  # 11

while True:
    s = input(">>> ")
    print(eval(s))