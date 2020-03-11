# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:23:39 2019

@author: jaideep
"""
car_prices=eval(input("Enter car prices:"))
discountset=set()
for i in car_prices:
        discount=i*(20/100)
        discountset.add(discount)
print(discountset)

    
