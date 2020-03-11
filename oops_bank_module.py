class bank:
    bank_names=["HDFC","ICICI","SBI"]
    hdfc_bank_account_no=range(1122,2234)
    icici_bank_account_no=range(4455,5567)
    sbi_bank_account_no=range(7788,8900)
    bank_address="hyd"
    bank_type=["savings","fixed","current"]
    def deposit(self,cus_bank_name,cus_account_no,cus_account_type,account_balance,account_deposit):
        self.bank_name=cus_bank_name
        self.account_no=cus_account_no
        self.account_type=cus_account_type
        if self.bank_name in bank.bank_names:
            if (self.account_no in bank.hdfc_bank_account_no) or (self.account_no in bank.icici_bank_account_no) or (self.account_no in bank.sbi_bank_account_no) and (self.account_type in bank.bank_type):
                self.available_balance=account_balance
                self.deposit_amount=account_deposit
                self.available_balance+=self.deposit_amount
                return self.bank_name,self.account_no,self.account_type,self.deposit_amount,self.available_balance
            else:
                return "Enter the correct credentials:"
        else:
            return "Enter the correct bank name:"
    def withdrawal(self,amount_withdrawal):
        self.withdrawal_amount=amount_withdrawal
        if self.bank_name in bank.bank_names:
            if (self.account_no in bank.hdfc_bank_account_no) or (self.account_no in bank.icici_bank_account_no) or (self.account_no in bank.sbi_bank_account_no) and (self.account_type in bank.bank_type):
                self.available_balance-=self.withdrawal_amount
                return self.withdrawal_amount,self.available_balance
            else:
                return "Enter the correct credentials:"
        else:
            return "Enter the correct bank name:"

