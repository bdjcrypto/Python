#Challenge 1: square a number

def squareMeBaby():
    """
    Words to explain below
    """
    x = input("Give x, get x^2...")
    x = int(x)
    x = x**2
    print(x)

squareMeBaby()

#Challenge 2: print what is input

def echo():
    x = input("'Echo' function ready...")
    print (x)

echo()

#Challenge 3: three required param, two optional
#               Rest is for fun

x = input("Give me a 1...")
y = input("Give me an 2...")
z = input("Give me an 3...")

def anal_fxn(x,y,z,a=6,b=9):
    x = int(x) * 30
    y = int(y) * 10
    z = int(z) * 7 - 2
    a = int(a)
    b = int(b)

    c = x + y + z
    print(a,b,c)

anal_fxn(x,y,z)

#Challenge 4: Double fxn

def first_fxn():
    x = input("Type any number below:")
    ans = float(x) / 2
    print (ans)

def second_fxn():
    y = input("Type any number below:")
    ans = float(y) * 4
    print (ans)

first_fxn()
second_fxn()

#Challenge 5: String to float, return print result

def word2num():
    x = input("Give me a numbie with a dessi")
    x = float(x)
    try:
        if(x == 69.69):
            print("Nice")
        else:
            print ("That's a stupid ass number")    
    except NameError:
        print("Yo, try again")

word2num()



#______________________________________________________________________________

#Challenge 6: Add docstrings to everything above

#______________________________________________________________________________




#Challenge 6.1: square a number

def squareMeBaby():
    x = input("Give x, get x^2...")
    x = int(x)
    x = x**2
    print(x)

squareMeBaby()

#Challenge 6.2: print what is input

def echo():
    x = input("'Echo' function ready...")
    print (x)

echo()

#Challenge 6.3: three required param, two optional
#               Rest is for fun

x = input("Give me a 1...")
y = input("Give me an 2...")
z = input("Give me an 3...")

def anal_fxn(x,y,z,a=6,b=9):
    x = int(x) * 30
    y = int(y) * 10
    z = int(z) * 7 - 2
    a = int(a)
    b = int(b)

    c = x + y + z
    print(a,b,c)

anal_fxn(x,y,z)

#Challenge 6.4: Double fxn

def first_fxn():
    x = input("Type any number below:")
    ans = float(x) / 2
    print (ans)

def second_fxn():
    y = input("Type any number below:")
    ans = float(y) * 4
    print (ans)

first_fxn()
second_fxn()

#Challenge 6.5: String to float, return print result

def word2num():
    x = input("Give me a numbie with a dessi")
    x = float(x)
    try:
        if(x == 69.69):
            print("Nice")
        else:
            print ("That's a stupid ass number")    
    except NameError:
        print("Yo, try again")

word2num()

