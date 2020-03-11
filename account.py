def account():
    acno=int(input("Enter account number:"))
    name=input("Enter your name:")
    curr_balance=float(input("Enter your current balance:"))
    transact_amount=float(input("Enter your transaction amount:"))
    transact_code=input("Enter your transact code")
    if(transact_code=='d'):
        print(name)
        print(acno)
        print("your current balance is :",curr_balance+transact_amount)
    elif (transact_code=='w'):
        print(name)
        print(acno)
        print("your current balance is :", curr_balance - transact_amount)
    else:
        print("Enter correct transactiom code:")

account()

