import bank_module as b
deposit=float(input("Enter the account deposit amount:"))
acc_no=int(input("Enter the customer account no:"))
acc_withdraw=float(input("Enter the account withdrawal amount:"))
result1=b.deposit(deposit,acc_no)
result2=b.withdraw(acc_withdraw,acc_no)
print("amount after deposit:",result1)
print("amount after withdrawal:",result2)
