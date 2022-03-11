#Chapter 12 Challenges

import math

#Challenge 1

class Apple:
    def __init__(self,w,c,s,t):
        self.weight = w
        self.color = c
        self.size = s
        self.taste = t
        print("New apple in the houseeeee!")
a1 = Apple(6.9,"red",3,"tart")
print(a1.weight,a1.color,a1.size,a1.taste)


#Challenge 2

class Circle:
    def __init__(self,r):
        self.radius = r
    def circ_area(self):
        return math.pi * self.radius ** 2

c1 = Circle(2)
print("c1 area = ", c1.circ_area())


#Challenge 3

class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h
    def tri_area(self):
        return 0.5 * self.base * self.height

t1 = Triangle(2,4)
print("t1 area = ", t1.tri_area())

#Challenge 4

class Hexagon:
    def __init__(self,s):
        self.side = s
    def calc_peri(self):
        return self.side * 6

h1 = Hexagon(9)
print("h1 perimeter = ",h1.calc_peri())
