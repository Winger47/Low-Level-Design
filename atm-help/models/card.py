from models.account import Account
from enums.card_status import CardStatus
from exceptions import InvalidPinError


class Card:
    def __init__(self,card_number:str,account:Account,pin:str):
        self.card_number=card_number
        self.account=account
        self.pin=pin
        self.status=CardStatus.ACTIVE

    def verify_pin(self,input_pin:str)->bool:
        return self.pin==input_pin      

    def change_pin(self,old_pin:str,new_pin:str)->None:
        if not self.verify_pin(old_pin):
            raise InvalidPinError(attempts_remaining=0)
        self.pin=new_pin  

    def block(self)->None:
        self.status=CardStatus.BLOCKED


    def is_blocked(self)->bool:
        return self.status==CardStatus.BLOCKED

    def __repr__(self):
        return f"Card(number={self.card_number}, status={self.status})"   

    

    