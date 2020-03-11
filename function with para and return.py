"""
Function with parameters and with return values

Data is taken as the parameters
"""

def deposit(cus_bank,cus_account,cus_account_type,deposit_amount):
    account_balance=500
    account_balance+=deposit_amount
    return account_balance, cus_account_type, cus_account, cus_bank # here return values are given so print statement is not needed
print(deposit('HDFC',11223355,'savings',10000))

