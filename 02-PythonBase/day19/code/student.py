
class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def __repr__(self):
        s = "Student(%s, %d, %d)" % (
            self.name, self.age, self.score)
        return s

L = []
L.append(Student("小张", 20, 100))
L.append(Student("小李", 18, 98))

print(L)
