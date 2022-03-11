#Chapter 8 Challenges


#Challenge 1

import statistics

import random

import Ch8C_Cubed

nums = []

for i in range(10):
    nums.append(random.randint(0,10000))

print(nums)

print("mean: ",statistics.mean(nums))
print("stdev: ",statistics.stdev(nums))


#Challenge 2
cube = int(input("Lemme cube ya \n: "))

print(Ch8C_Cubed.cubed(cube))

