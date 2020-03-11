"""
Function without parameters and with return values
"""



def deposit():
    bank_name='HDFC'
    bank_account=1122334455
    bank_type='savings'
    account_balance=500.00
    deposit_amount=float(input("Enter the deposit amount:"))
    account_balance+=deposit_amount
    return account_balance,bank_account,bank_name,bank_type
print(deposit())
