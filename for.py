# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:52:38 2019

@author: jaideep
"""

num = int(input("Enter an integer"))
if num>0 and num<=50:
    for i in range(1,21):
        p=i*num
        print(i,'*',num,'=',p)
else:
    print("Enter a number less than 50 and greater than zero")