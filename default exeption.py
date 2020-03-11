"""
 @ Default execption can handle all exceptions.
"""
try:
    a=int(input("Enter a integer:"))
    b=int(input("Enter b integer:"))
    print("Division:",a/b)  #execption causing line or problematic line
except:             #Default except block program
    print("Plz enter valid input")
print("Addition:",a+b)
print("Substraction:",a-b)
print("multiplication:",a*b)
print("Power:",a**b)
