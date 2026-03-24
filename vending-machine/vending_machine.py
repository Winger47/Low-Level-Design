from inventory import Inventory
from vending_state import IdleState

class VendingMachine:
    def __init__(self):
        self.inventory = Inventory()
        # The machine always starts in the Idle state:
        self.state = IdleState(self)  
        self.balance = 0
        self.selected_item = None

    def set_state(self, state):
        self.state = state
        
    def add_balance(self, amount):
        self.balance += amount
        
    def set_selected_item(self, code):
        self.selected_item = self.inventory.get_item(code)
        
    def refund_balance(self):
        print(f"Refunding: {self.balance} coins")
        self.balance = 0
        
    def reset(self):
        self.balance = 0
        self.selected_item = None

    # --- Actions the user actually calls on the machine ---
    def insert_coin(self, coin):
        self.state.insert_coin(coin)
        
    def select_item(self, code):
        self.state.select_item(code)
        
    def dispense(self):
        self.state.dispense()
        
    def refund(self):
        self.state.refund()
