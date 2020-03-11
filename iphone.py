# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:28:19 2019

@author: jaideep
"""

iphone_price = float(input("Enter the price of the iphone"))
if iphone_price > 150000:
    discount = iphone_price *(15/100)
    iphone_price = iphone_price-discount
    print("iphone price =",iphone_price)
elif iphone_price < 149000 and iphone_price > 100000:
    discount = iphone_price *(14/100)
    iphone_price = iphone_price-discount
    print("iphone price =",iphone_price)
elif iphone_price < 99999 and iphone_price>50000:
    discount = iphone_price *(13/100)
    iphone_price = iphone_price-discount
    print("iphone price =",iphone_price)
else:
    discount = iphone_price *(13/100)
    iphone_price = iphone_price-discount
    print("iphone price =",iphone_price)
