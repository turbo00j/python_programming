# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:32:23 2019

@author: jaideep
"""
def marks():
    python_marks=int(input("Enter the python marks:"))
    if python_marks > 100:
        print("Entered marks is above 100 (max marks=100)")
    elif python_marks == 100:
        print("Grade A+")
    elif python_marks>=80 and python_marks<=89:
        print("grade A")
    elif python_marks>=70 and python_marks<=79:
        print("Grade B+")
    elif python_marks>=60 and python_marks<=69:
        print("Grade B")
    elif python_marks>=50 and python_marks<=59:
        print("Grade C+")
    elif python_marks>=40 and python_marks<=49:
        print("Grade C")
    else:
        print("Fail")
marks()