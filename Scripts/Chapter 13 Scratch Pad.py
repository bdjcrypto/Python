#Challenge 13 Scratch Pad

import math

#Encapsulation Practice

class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.length = l
        print("Created {} by {} rectangle!".format(self.width,self.length))

    def area(self):
        return self.width * self.length

    def hypotenuse(self):
        return math.sqrt(self.width**2 + self.length**2)

r1 = Rectangle(3,4)
print("area = {}".format(r1.area()), "\nhypotenuse length = {}".format(r1.hypotenuse()))

