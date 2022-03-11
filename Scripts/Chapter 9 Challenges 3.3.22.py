#Chapter 9 Challenges

import os

import csv

"""
#Challenge 1 & 2

with open(("Challenge9.1.csv",'w') as f:
    for rows in f:
        r = csv.writer(f,delimiter = ',')



with open("Challenge9.1.csv",'r') as f:
    r = csv.reader(f,delimiter = ',')
    for row in r:
        print(' | '.join(row))
"""

#Challenge 2 & 3

print("Let's make a table")
cols = int(input("How many columns?"))
rows = int(input('How many rows?'))

listOfRows = [[] for r in range(rows)]
for r in range(rows):
    currentRow = listOfRows[r]
    print("input row number " + str(r+1) + " values")
    for c in range(cols):
        cell = input("cell " + str(c+1) + '.' + str(r+1) + ' ')
        currentColumn = currentRow.append(cell)
print(listOfRows)

with open("Challenge9.1.csv",'w',newline='') as f:
    w = csv.writer(f,delimiter = ',')
    for r in range(rows):    
        klist = listOfRows[r]
        w.writerow(klist)

