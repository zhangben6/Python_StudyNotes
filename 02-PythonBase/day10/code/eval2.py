# eval2.py

s= "x + y"

d1 = {"x":100, 'y':200}
d2 = {"x":1}

v = eval(s, d1, d2)

print(v)

