# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:16:05 2019

@author: jaideep
"""

company_name = input("Enter the company name :")
company_address = input("Enter the company address :")
company_Email = input("Enter the company Email :")
def employee():
    employee_ID = input("Enter the ID of the employee :")
    employee_name = input("Enter the NAME of the employee :")
    employee_dept = input("Enter the DEPARTMENT of the employee :")
    employee_designation = input("Enter the DESIGNATION of the employee :")
    employee_salary = input("Enter the SALARY of the employee :")
    print("EMPLOYEE ID :",employee_ID,"\nEMPLOYEE NAME :",employee_name,"EMPLOYEE DEPARTMENT :",employee_dept,"EMPLOYEE DESIGNATION :",employee_designation,"EMPLOYEE SALARY :",employee_salary)
def display():
    employee()
    
    print("COMPANY NAME :",company_name,"\nCOMPANY ADDRESS :",company_address,"\nCOMPANY EMAIL :",company_Email)

display()