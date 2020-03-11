def big():
    a=int(input('Enter a :'))
    b=int(input('Enter b :'))
    c = int(input('Enter c :'))
    if (a>b and a>c):
        print(" A is big")
    elif (b>a and b>c):
        print(" B is big")
    else:
        print("C is big")
big()