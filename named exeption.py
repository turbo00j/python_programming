try:
    a=int(input("Enter a integer:"))
    b=int(input("Enter b integer:"))
    print("Division:",a/b)  #execption causing line or problematic line
except ZeroDivisionError:   #Named except block
    print("A number cannot be divisible by zero") #exception handling line or solution line
except ValueError:
    print("Enter only an integer:")
print("Addition:",a+b)
print("Substraction:",a-b)
print("multiplication:",a*b)
print("Power:",a**b)
