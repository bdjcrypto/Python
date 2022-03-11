#Chapter 9 Scratch Pad
"""
import os
os.path.join("Users","bob","st.txt")

st = open("st.txt","w")
st.write("Hi from Python!")
st.close()


with open("st.txt","w") as f:
    f.write("Hi from Python! (with)")

mylist = []

with open("st.txt","r") as f:
    mylist.append(f.read())
print(mylist)
"""

import csv

with open("st.csv","w",newline="") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(["Date","Description","Category"])
    w.writerow(["3/3/2022","Monke Balls","Nonsense"])
    
with open("st.csv",'r') as f:
    r = csv.reader(f,delimiter = ',')
    for row in r:
        print(' | '.join(row))
