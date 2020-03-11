aadharcard_numbers=range(1122334455,5566778900)
try:
    cus_aadhar=int(input("Enter your aadhar number:"))
    if cus_aadhar in aadharcard_numbers:
        print(cus_aadhar,"is correct")
    else:
        print("Plz enter correct aadhar number:")
except ValueError:
    print("plz Enter only integer value:")
