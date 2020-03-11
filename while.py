# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:03:34 2019

@author: jaideep
"""

company_names=eval(input("Enter ur company names:"))
print("@"*30)
print("Company names are :",company_names)
ans="YES"
while ans=="YES":
    existed_company=input("After which company u want to add the new company name :")
    i=company_names.index(existed_company)
    print("index is :",i)
    new_company=input("Enter a new company name :")
    company_names.insert(i+1,new_company)
    print("Company names :",company_names)
    ans=input("Enter your decision YES/NO :")
    