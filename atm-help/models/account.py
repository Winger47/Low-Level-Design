from models.user import User
from exceptions import InsufficientFundsError



class Account:
    """A bank account with balance and basic transaction operations."""
    def __init__(self,user:User,account_id:str,balance:float=0.0):
        self.user=user
        self.account_id=account_id
        self.balance=balance
    def withdraw(self,amount:float)->None:
        if amount<=0:
            raise ValueError("Amount must be positive")
        if amount>self.balance:
            raise InsufficientFundsError(amount,self.balance)
        self.balance-=amount        
    def deposit(self,amount:float)->None:
        if amount<=0:
            raise ValueError("Amount must be positive")
        self.balance+=amount
    def get_balance(self)->float:
        return self.balance

    def __repr__(self):
        return f"Account(id={self.account_id}, balance={self.balance})"     
        

        