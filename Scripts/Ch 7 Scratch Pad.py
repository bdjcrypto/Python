#Chapter 7: Loops - Scratch Pad

name = input("What's yo name? \n: ")
for ch in name:
    print(ch)

favs = ["Empire Strikes Back","The Red Wedding","Michael burns foot on George Foreman grill"]
for show in favs:
    print(show)

for i, show in enumerate(favs):
    new = favs[i]
    new = new.upper()
    favs[i] = new
print(favs)

import time
n = True
while n == True:
    for i in range(10):
        time.sleep(i/10)
        print("elephant cock and a tiny little pair of squirrel balls")
    n = False
print("okay, I'm done")

