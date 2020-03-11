# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:35:43 2019

@author: jaideep
"""
                        
halltickets = range(11223344,44556678)
exam_centers = ["Ameerpet ABC engg.clg","SRnagar XYZ engg.clg","Kukataplly RSS engg.clg"]
student_hallticket = int(input("Enter your hallticket number:"))
if student_hallticket in halltickets:
    print("HALL TICKET NUMBER is valid")
    student_exam = input("Enter your EXAM CENTER:")  
    if student_exam in exam_centers :
        print ("EXAM CENTER is valid")
        print("#"*30)
        print("ALL THE BEST")
        print("#"*30)
    else:
        print("Dear student, Enter valid exam center ")
else:
    print("Dear student, Enter valid hall ticket number")
