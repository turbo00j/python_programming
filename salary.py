# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:34:09 2019

@author: jaideep
"""
class salary:
    def __init__(self):
        self.salary=float(input("Enter the salary:"))
        self.hike=float(input("Enter the salary hike :"))
        print("salary :",self.salary)
    def display_salary(self):
        self.salary = self.salary+self.hike
        print("salary after hike:",self.salary)
e1=salary()
e1.display_salary()