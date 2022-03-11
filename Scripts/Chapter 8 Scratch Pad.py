import math

import random

import statistics

import keyword

print(math.pow(2,3))

n = 0
while n != 69:
    n = random.randint(-70,70)
    print(n)
print("...Nice")

nums = [1,5,33,12,46,33,2]
print(nums)
print("mean: ",statistics.mean(nums))
print("median: ", statistics.median(nums))
print("mode: ",statistics.mode(nums))

print(keyword.iskeyword("for"))
print(keyword.iskeyword("nipple"))

"""
Rest of scratch pad can be found in the 'tstp' folder.
'hello', 'project 1', 'module1', and 'module2' were used to test imports of your own files.
The imports above are native to Python."
"""
