# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:53:50 2019

@author: jaideep
"""

pin=range(1122,3345)
i=1
while i<=3:
    n=int(input("Enter ur pin:"))
    if n in pin:
        print("Your pin is valid")
        break
    else:
        print("Enter valid pin")
    i=i+1
else:
    print("Your account is blocked")
    