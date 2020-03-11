# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:04:00 2019

@author: jaideep
"""

ans='yes'
while ans=='yes':
    n=int(input("Enter an integer:"))
    if n<=0 or n>=100:
        print("please enter the numbers less than 100 and more than 0:")
        continue
    else:
        for i in range(1,21):
            print(i,'*',n,'=',i*n)
    ans=input("Do you want to enteran number  for which multipication should be done(yes/no):")
