from datetime import datetime
from typing import Optional
from models.account import Account
from enums import TransactionType, TransactionStatus

class Transaction:
    def __init__(self, transaction_id:str, account:Account, transaction_type:TransactionType, amount:Optional[float]=None) -> None:
        self.transaction_id = transaction_id
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()              # internal
        self.status = TransactionStatus.PENDING      # internal 

    def mark_success(self)->None:
        self.status=TransactionStatus.SUCCESS

    def mark_failed(self,reason: str = "")->None:
        self.status=TransactionStatus.FAILED
        self.reason=reason    
        

    def __repr__(self):
        return f"<Transaction {self.transaction_id} {self.transaction_type.name} amount={self.amount} status={self.status.name}>"
           