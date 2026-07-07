class BankAccount:
    def __init__(self,AccountNumber,name,balance):
        self.AccountNumber=AccountNumber
        self.holderName=name
        self.balance=balance
        self.bankfee(balance)

    def deposite(self,amount_deposite):
        if amount_deposite>=0:
            self.balance+=amount_deposite
            self.bankfee(amount_deposite)

    def withdrawal(self,amount_withdrawal):
        if amount_withdrawal>=0 and amount_withdrawal<=self.balance:
            self.balance-=amount_withdrawal

    def bankfee(self,amount):
        fee=amount*0.05
        self.balance-=fee

    def display(self):
        print("Account Number : ",self.AccountNumber)
        print("name : ",self.holderName)
        print("balance : ",self.balance)

new_user=BankAccount(123456,"ankit",5000)
new_user.display()
new_user.deposite(5000)
new_user.display()
new_user.withdrawal(5000)
new_user.display()
            