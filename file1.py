f=open("Employee.txt",'w')
"""
open function is used to open the file in specified mode
e.g; in the above line open function is used to open employee.txt file in 'w' mode

open() : open function performs two responsibilities
1.if file is existed it opens the existed file in specified mode.
2.if file is not existed it created the new file and opens it in specified mode.
"""
f.write("E1122,Raju,IT,SE,10000.00\n")
f.write("E2233,Rani,IT,SE,10000.00\n")
print("Employee records are written succesfully")
f.close()
