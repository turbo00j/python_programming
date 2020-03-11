bank_name="HDFC"
bank_IFSC="HDFC1256"
account_no = range(11223344,22334456)
bank_address="hyd"
account_balance=float(input("Enter the account balance:"))
def deposit(amount_deposit,cus_account_no):
    global account_no
    global account_balance
    if bank_name=="HDFC" and bank_IFSC=="HDFC1256" and cus_account_no in account_no and account_balance>=10000.00 :
        account_deposit=amount_deposit
        account_balance+=account_deposit
        return bank_name,bank_IFSC,bank_address,account_deposit,account_balance
    else:
        print("Enter the correct details")
def withdraw(amount_withdraw,cus_account_no):
    global account_balance
    if bank_name=="HDFC" and bank_IFSC=="HDFC1256" and cus_account_no in account_no and account_balance>=10000.00 :
        account_withdraw=amount_withdraw
        account_balance -= account_withdraw
        return account_withdraw,account_balance
    else:
        print("Enter valid details:")