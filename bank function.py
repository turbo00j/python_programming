Bank_names=['HDFC','ICICI']
account_numbers_HDFC=range(11223345,55667789)
account_numbers_ICICI=range(4455667789,5566778900)
account_types=['savings','current','fixed']
cus_bank_name=input("Dear customer,Enter your Bank name:")
cus_account_number=int(input("Dear customer,Enter your account number:"))
cus_account_type=input("Dear customer,Enter your Bank type:")
def customer_details(cus_bank_name,cus_account_number,cus_account_type):
    if (cus_bank_name=='HDFC' and cus_account_number in account_numbers_HDFC) or (cus_bank_name=='ICICI' and cus_account_number in account_numbers_ICICI) and (cus_account_type in account_types):
        print("Your account details are valid,plz perform operations")
        Account_balance=500
        Deposit_amount=float(input("Enter deposit amount:"))
        Account_balance+=Deposit_amount
        return Account_balance
    else:
        print("Enter valid account details")
print(customer_details(cus_bank_name,cus_account_number,cus_account_type))    
        


