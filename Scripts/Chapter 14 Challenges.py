#Chapter 14 Challenges

#Challenge 1

class Square():
    square_list = []    

    def __init__(self,s):
        self.side = s
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}\n".format(self.side,self.side,self.side,self.side)

s1 = Square(4)
s2 = Square(2)
s3 = Square(8)

print(Square.square_list)
print(s1,s2,s3)

def compare_shapes(a,b):
    if a == b:
        return True
    else:
        return False

print(compare_shapes(s1,s1))
