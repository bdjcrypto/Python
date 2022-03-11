"""
#Chapter 7 Challenges

#Challenge 1

shows = ["The Walking Dead","Entourage","The Sopranos","The Vampire Diaries"]
for i in range(len(shows)):
    print(shows[i])


#Challenge 2

for i in range(25,51):
    print(i)


#Challenge 3

for i in range(len(shows)):
    print(shows[i],i)


#Challenge 4

import random
while True:
    answer = int(random.randint(1,11))
    print(answer)
    guess = input("Guess a number between 1 and 10. Enter q to quit \n: ")
    if guess == "q":
        break
    else:
        try:
            guess = int(guess)
        except ValueError:
            print("Try again")
            continue
    if guess == answer:
        print("You win!")
    else:
        print("Try again")
        continue
"""

#Challenge 5

a_list = [8,19,148,4]
b_list = [9,1,33,83]
c_list = []

for a in a_list:
    for b in b_list:
        c_list.append(a*b)
print(c_list)
