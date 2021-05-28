class Bank:

    def __init__(self,name,account,pin):
              self.name=name
              self.account=account
              self.pin=pin
    def deposite(self):
        return f"You have deposited money in{self.name} bank and your account number is{self.account}"
    def freez(self):
        return f"Dear customer this is from {self.name},your account number{self.account} with pin{self.pin}has been frozen"
