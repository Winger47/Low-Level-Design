from enums import Denomination
from exceptions import InsufficientCashInATMError

class CashDispenser:
    def __init__(self,inventory: dict[Denomination, int]):
        self.inventory=inventory  
    
    def dispense(self, amount: int) -> dict[Denomination, int]:
        # Pass 1: plan (read-only)
        plan = { }
        remaining = amount
        denoms_sorted = sorted(self.inventory.keys(), key=lambda d: d.value, reverse=True)
    
        for d in denoms_sorted:
            if remaining == 0:
                break
            notes_needed = remaining // d.value
            notes_available = self.inventory[d]
            notes_to_use = min(notes_needed, notes_available)
            if notes_to_use > 0:
                plan[d] = notes_to_use
            remaining -= notes_to_use * d.value
    
        # Validate
        if remaining > 0:
            raise InsufficientCashInATMError(amount)
    
        # Pass 2: deduct (write)
        for d, count in plan.items():
            self.inventory[d] -= count
    
        return plan

    def add_cash(self, denom: Denomination,count:int) -> None:  
        self.inventory[denom] = self.inventory.get(denom, 0) + count  

    def total_cash(self)->int:
        return sum(d.value * count for d, count in self.inventory.items()) 

    def __repr__(self)->str:
        return f"CashDispenser({self.inventory})" 