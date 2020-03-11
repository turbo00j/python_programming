# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:05:19 2019

@author: jaideep
"""
pin=range(1122,3345)
for i in range(1,4):
    n=int(input("Enter ur pin:"))
    if n in pin:
        print("Your pin is valid")
        break
    else:
        print("Enter valid pin")
else:
    print("Your account is blocked")
    