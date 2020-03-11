# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:08:24 2019

@author: jaideep
"""
class product:
    def __init__(self,pno,pname,pcompany,pprice):
        self.product_ID=pno
        self.product_name=pname
        self.product_company=pcompany
        self.product_price=pprice
    def display(self):
        print("*"*50)
        print(self.__dict__)
        print("*"*50)
p1=product(1122,'samsung s6','samsung',50000.00)
p1.display()

p2=product(2233,'htc h5','HTC',1000000.00)
p2.display()
        
