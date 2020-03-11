class person:
    def __init__(self):
        self.studentname=input("Enter the student name:")
        self.studentmobile=int(input("Enter the student mobile:"))
class student(person):
    def student_details(self):
        person.__init__(self)
        self.studentID=input("Enter the student ID:")
        self.studentcourse=input("Enter the student course:")
        self.coursefee=float(input("Enter the student course fee:"))
    def fee_structure(self):
        self.course_fee=3000.00
        self.CGST=self.course_fee*(4/100)
        self.SGST=self.course_fee*(2/100)
        self.final_course_fee=self.course_fee+self.CGST+self.SGST
    def print(self):
        print('*'*30)
        print("*** STUDENT INFORMATION ***")
        print('*' * 30)
        print(self.__dict__)
        print("CGST:",self.CGST)
        print("SGST:", self.SGST)
        print("final fee:",self.final_course_fee)
s1=student()
s1.student_details()
s1.fee_structure()
s1.print()

s2=student()
s2.student_details()
s2.fee_structure()
s2.print()
