# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:37:13 2019

@author: jaideep
"""

book_prices=eval(input("Enter the books prices:"))
book_prices_set=set()
for i in book_prices:
    total_GST=i*(2/100)+i*(4/100)
    discount=i*(2/100)
    i=(i+total_GST)-discount
    book_prices_set.add(i)
print(book_prices_set)
final_book_list=list(book_prices_set)
print(final_book_list)
print(type(final_book_list))
final_book_list2=tuple(book_prices_set)
print(final_book_list2)
print(type(final_book_list2))