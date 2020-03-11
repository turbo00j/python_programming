# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:02:53 2019

@author: jaideep
"""

class employee:
    def __init__(self):
        self.empid=input("Enter employee ID:")
        self.empname=input("Enter Employee name:")
        self.empdept=input("Enter Employee department:")
        self.empdesg=input("Enter Employee designation:")
        self.empsalary=float(input("Enter Employee salary:"))
    def Display_emp_info(self):
        print('*'*30)
        print(self.__dict__)
        print('*'*30)
    def display_salary(self)   :
        hike=float(input("Enter the salary hike :"))
        self.empsalary=hike+self.empsalary
        print("salary after hike :",self.empsalary)
    def allowances(self):
        TA=float(input("Enter the travelling allowance:"))
        DA=float(input("Enter the dearness allowance :"))
        self.empsalary=TA+DA+self.empsalary
        print("Final salary :",self.empsalary)
e1=employee()
e1.Display_emp_info()
e1.display_salary()
e1.allowances()
