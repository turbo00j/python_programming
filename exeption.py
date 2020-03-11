# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:16:35 2019

@author: jaideep
"""
# WITH EXCEPTION
a=10
b=0
try:
    print("Division:",a/b)  #execption causing line or problematic line
except ZeroDivisionError:   #Named except block
"""
 @ Named execption can only handle that named exception only.
"""
    print("A number cannot be divisible by zero") #exception handling line or solution line
print("Addition:",a+b)
print("Substraction:",a-b)
print("multiplication:",a*b)
print("Power:",a**b)

"""
WITHOUT EXEPTION
a=10
b=0
print("Division:",a/b) 
print("Addition:",a+b)
print("Substraction:",a-b)
print("multiplication:",a*b)
print("Power:",a**b)

"""
