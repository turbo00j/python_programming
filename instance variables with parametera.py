# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:46:11 2019

@author: jaideep
"""
class product:
    def product_info(self,pno,pname,pcompany,pprice):
        self.product_ID=pno
        self.product_name=pname
        self.product_company=pcompany
        self.product_price=pprice
    def display(self):
        print(self.__dict__)
p1=product()
a=int(input("Enter pno:"))
b=input("Enter pname:")
c=input("Enter comonay:")
d=float(input("Enter price:"))
p1.product_info(a,b,c,d)
p1.display()

        
