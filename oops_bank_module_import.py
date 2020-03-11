import oops_bank_module


cus_bank_name=input("Enter customer bank name :")
cus_account_no=int(input("Enter customer bank account number:"))
cus_account_type=input("Enter the customer account type:")
account_balance=float(input("Enter the customer account balance:"))
account_deposit=float(input("Enter customer account depositing amount:"))
amount_withdrawal=float(input("Enter customer account withdrawal amount:"))
obj=oops_bank_module.bank()
obj.deposit(cus_bank_name,cus_account_no,cus_account_type,account_balance,account_deposit)
obj.withdrawal(amount_withdrawal)

print("account balance :",available_balance)
