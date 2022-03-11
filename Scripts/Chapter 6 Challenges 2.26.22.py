"""
#Challenge 1

word = "Camus"
for i in range(5):
    print(word[i])
    i += 1


#Challenge 2

a = input("gimme word: ")
b = input("who you talk shit about?: ")

s = "Yesterday I wrote a " +  a + ". I sent it to " + b
print(s)


#Challenge 3

c = "aldous Huxley was born in 1894."
c = c.replace("a","A")
print(c)


#Challenge 4

d = "Where now? Who now? When now?"
dlist = d.split("? ")
print(dlist)


#Challenge 5

elist = ["The","fox","jumped","over","the","fence","."]

e = elist[0:6]
e = " ".join(e)

print(e + ".")


#Challenge 6

s1 = "A screaming comes across the sky."
sdolla = s1.replace("s","$")
print(sdolla)


#Challenge 7

#solution 1
h = "Hemingway"
loc = -1
for i in range(len(h)):
    if h[i] == "m":
        loc = i + 1
        loc_s = str(loc)
        print("first 'm' at location " + loc_s)
    else:
        continue
if loc == -1:
    print("no 'm' found")

#solution 2 (index)
h = "Hemingway"
try:
    print("first 'm' located at:")
    print(h.index("m"))
except ValueError:
    print("no 'm' found")
    
#Challenge 8

bookquote = "This was too easy of an assignment for this far along in the book"
print(bookquote)

#Challenge 9

t = "three "
print(t + t + t)
print(t*3)
"""

#Challenge 10

c10 = "It was a bright cold day in April, and the clocks were striking thirteen."
slyce = c10.index(",")
print(c10[:slyce] + ". And my nips were roq hard")









































