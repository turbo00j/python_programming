account_numbers=range(1122334455,5566778900)
ans='yes'
while ans=='yes':
    cus_account=int(input("Enter your account number:"))
    if cus_account in account_numbers:
        print("Your account no is valid ,plz perform the operstions ")
    else:
        print("plz give valid account number:")
        continue
    ans=input("Do you want to enter another account no(yes/no):")
                    
    
