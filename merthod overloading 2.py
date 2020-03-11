class bank:

    def deposit(self,bank_name,bank_account,bank_deposit,deposit_type):
        print("bank name:",bank_name)
        print("bank account:",bank_account)
        print("deposit amount:",bank_deposit)
        print("deposit_type:",deposit_type)
b1=bank()
b1.deposit('HDFC','savings',50000.00,'cash',)
print('*'*30)
b1.deposit('HDFC','current',800.00,'DD')
print('*'*30)
b1.deposit('HDFC','fixed','50gms','gold')


