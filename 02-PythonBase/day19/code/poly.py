# poly.py

class Shape:
    def draw(self):
        print("Shape.draw被调用")
class Point(Shape):
    def draw(self):
        print("Point.draw被调用")
class Circle(Point):
    def draw(self):
        print("Circle.draw被调用")



def mydraw(s):
    s.draw()  #  此处会根据s绑定对象的类型来决定调用谁?
s1 = Circle()
s2 = Point()
mydraw(s2)
mydraw(s1)

