#Chapter 13 Challenges

import math

#Challenge 1

class Rectangle():

    def __init__(self,l,w):
        self.len = l
        self.width = w
        print("Created rectangle! {} by {}".format(self.len,self.width))

    def calc_peri(self):
        return self.len * 2 + self.width * 2

class Square():

    def __init__(self,s):
        self.side = s
        print("Created square! Side length = {}".format(self.side))

    def calc_peri(self):
        return self.side * 4

    def change_size(self):
        delta = int(input("If you would like to change the size of the square, enter the amount of increase \n: "))
        self.side = self.side + delta
        return self.side

r1 = Rectangle(3,4)
s1 = Square(5)

print("Perimeters are as follows\n","{} : {}\n".format(r1,r1.calc_peri()),"{} : {}\n".format(s1,s1.calc_peri()))

#Challenge 2

print("New side length: ",s1.change_size())

