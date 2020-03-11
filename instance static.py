# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:42:53 2019

@author: jaideep
"""

class institute:
    institute_name="SAI SPURTHI"
    institute_address="spl"
    institute_code="C5"
    institute_website="www.ssit.com"
    def student_info(self):
        self.student_name=input("Enter the student name:")
        self.student_id=input("Enter the student ID:")
        self.student_branch=input("Enter the student branch:")
        self.student_mobile=int(input("Enter the student mobile number:"))
    def display(self):
        print("Institute name :",institute.institute_name)
        print("Institute address :",institute.institute_address)
        print("Institute code :",institute.institute_code)
        print("Institute website :",institute.institute_website)
        print("Student name :",self.student_name,"\n Student ID:",self.student_id,"\n Student branch:",self.student_branch,"\n Student mobile number:",self.student_mobile)

s1=institute()
s1.student_info()
print("@"*50)
s1.display()
print("@"*50)

s2=institute()
s2.student_info()
print("@"*50)
s2.display()
print("@"*50)