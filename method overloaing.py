class bank:
    def deposit(self,bank_name,bank_account,bank_IFSc,cash_depositamount,dd_no,dd_deposit,gold_deposit_amount,cheque_no,cheque_amount):
        self.Bank_name=bank_name
        self.Bank_account=bank_account
        self.bank_IFSc=bank_IFSc
        self.cash_depositamount=cash_depositamount
        self.dd_no=dd_no
        self.dd_deposit=dd_deposit
        self.gold_deposit_amount=gold_deposit_amount
        self.cheque_amount=cheque_amount
        self.cheque_no=cheque_no
        print(self.__dict__)
o1=bank()
p="HDFC"
q=11223344
r="hdfc1234"
s=10000.00
t='DD1256'
u=250000.00
v="250gms"
w="ch1234"
x=500000.00

o1.deposit(p,q,r,s,None,None,None,None,None)
o1.deposit(p,q,r,None,t,u,None,None,None)
o1.deposit(p,q,r,None,None,None,v,None,None)
o1.deposit(p,q,r,None,None,None,None,w,x)
