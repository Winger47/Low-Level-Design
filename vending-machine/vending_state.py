from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from coin import Coin



class VendingMachineState(ABC):
    def __init__(self,machine):
        self.machine=machine
    
    @abstractmethod
    def select_item(self,code:str)->None:
        pass
    def dispense(self)->None:
        pass
    def insert_coin(self,coin:Coin)->None:
        pass
    def refund(self)->None:
        pass
class IdleState(VendingMachineState):

    def insert_coin(self,coin:Coin)->None:
        print("Please select an item before inserting")
    def select_item(self,code:str):
        item = self.machine.inventory.get_item(code)
        if not item:
            print("Item not found")
            return
        
        self.machine.set_selected_item(code)
        
        self.machine.set_state(ItemSelectedState(self.machine))
        print(f"Item {code} selected. Please insert {item.price} coins")

    

    def dispense(self)->None:
        print("No item selected.")

    

    def refund(self)->None:
        print("No money to refund.")

class ItemSelectedState(VendingMachineState):
    def insert_coin(self,coin:Coin)->None:
        self.machine.add_balance(coin.get_value())
        print(f"coin inserted: {coin.get_value()}. Total balance: {self.machine.balance}")

        selected_item=self.machine.selected_item
        
        if selected_item and self.machine.balance>=selected_item.price:
            self.machine.set_state(HasMoneyState(self.machine))
    def select_item(self, code: str):
        print("Item already selected. Please insert money or request refund to select a different item.")
    
    def dispense(self):
        print("Please insert sufficient money.")
        
    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        self.machine.set_state(IdleState(self.machine))

class HasMoneyState(VendingMachineState):
    def insert_coin(self, coin: Coin):
        self.machine.add_balance(coin.get_value())
        print(f"coin inserted: {coin.get_value()}. Total balance: {self.machine.balance}")
    
    def select_item(self, code: str):
        print("Item already selected. Please insert money or request refund to select a different item.")
    
    def dispense(self):
        print("Sufficient money confirmed. Proceeding to dispense...")
        self.machine.set_state(DispenseState(self.machine))

    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        self.machine.set_state(IdleState(self.machine))

class DispenseState(VendingMachineState):
    def insert_coin(self, coin: Coin):
        print("Please select an item before inserting")
    def select_item(self, code: str):
        print("Item already selected. Please insert money or request refund to select a different item.")
    
    def dispense(self):
        print("Dispensing item...")
        selected_code = self.machine.selected_item.code if hasattr(self.machine.selected_item, 'code') else self.machine.selected_item
        if hasattr(self.machine.inventory, 'reduce_stock'):
            self.machine.inventory.reduce_stock(selected_code)
        self.machine.reset()
        self.machine.set_state(IdleState(self.machine))
        
    def refund(self):
        print("No money to refund.")
        self.machine.reset()
        self.machine.set_state(IdleState(self.machine))
        
    
        
        
    
    