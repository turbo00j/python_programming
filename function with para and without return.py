"""
Function with parameters and without return values
"""


def deposit(cus_bank,cus_account,cus_account_type,deposit_amount):
    account_balance=500
    account_balance+=deposit_amount
    print("Account_balance:",account_balance)
    print("bank name:",cus_bank)    #no return value so we have given print inorder to give the output
print(deposit('HDFC',11223355,'savings',10000))

