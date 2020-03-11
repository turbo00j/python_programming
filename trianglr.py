a=int(input("Enter the angle a:"))
b=int(input("Enter the angle b:"))
c=int(input("Enter the angle c:"))
if (a==b==c):
    print("given triangle is equilateral")
elif(a==b!=c or a!=b==c):
    print("given triangle is iscoceles ")
elif(a!=b!=c):
    print("Given triangle is scalen")