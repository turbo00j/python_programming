a=b=None
try:
    a=float(input("Enter a:"))
    b=float(input("Enter b:"))
    print(a*b)
    print(a+b)
except:
    print("Enter valid float integers:")
finally:
    del a,b
print(a,b)