# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:45:42 2019

@author: jaideep
"""

class employee:
    def __init__(self,eno,ename,edept,edesg,esalary):
        self.empid=eno
        self.empname=ename
        self.empdept=edept
        self.empdesg=edesg
        self.empsalary=esalary
    def Display_emp_info(self):
        print('*'*30)
        print(self.__dict__)
        print('*'*30)
e1=employee('E1122','RAJU',"IT","manager",100000)
e1.Display_emp_info()
